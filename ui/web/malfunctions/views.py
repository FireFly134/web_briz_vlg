from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import (
    HttpRequest,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from django_stubs_ext import QuerySetAny

from .forms import (
    CreateMalfunctionsForm,
    UpdateModelMalfunctionsForm,
)
from .models import ModelMalfunctions


class MalfunctionsList(ListView):
    model = ModelMalfunctions
    template_name = "malfunctions/list.html"
    context_object_name = "list"

    def get_queryset(
        self,
    ) -> QuerySetAny[ModelMalfunctions, ModelMalfunctions]:
        return ModelMalfunctions.objects.all()


class MalfunctionsUpdate(UpdateView):
    model = ModelMalfunctions
    form_class = UpdateModelMalfunctionsForm
    template_name = "malfunctions/edit.html"
    pk_url_kwarg = "info_id"
    context_object_name = "info"
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        report = form.save(commit=False)

        # Рассчитываем время простоя, если есть время завершения
        if report.date_time_closed:
            downtime = report.date_time_closed - report.date_time_accepted
            report.simple = int(downtime.total_seconds() / 60)

        report.save()

        return super().form_valid(form)


@login_required
def delete_contact(
    request: HttpRequest, info_id: int
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    info = ModelMalfunctions.objects.get(pk=info_id)
    if request.user.is_superuser:
        info.delete()
        return redirect("list")
    raise PermissionDenied()

@login_required
def send_archive(
    request: HttpRequest, info_id: int
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    info = ModelMalfunctions.objects.get(pk=info_id)
    if request.user.is_superuser:
        # изменяем значение поля status на False
        info.status = False
        # сохраняем изменения в базе данных
        info.save()
        return redirect("list")
    raise PermissionDenied()

@login_required
def send_black(
    request: HttpRequest, info_id: int
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    info = ModelMalfunctions.objects.get(pk=info_id)
    if request.user.is_superuser:
        # изменяем значение поля status на False
        info.status = True
        # сохраняем изменения в базе данных
        info.save()
        return redirect("list")
    raise PermissionDenied()


class MalfunctionsCreate(CreateView):
    model = ModelMalfunctions
    form_class = CreateMalfunctionsForm
    template_name = "malfunctions/create.html"
    success_url = reverse_lazy("list")

    def form_valid(self, form: CreateMalfunctionsForm):
        report = form.save(commit=False)
        report.save()

        # Рассчитываем время простоя, если есть время завершения
        if report.date_time_closed:
            downtime = report.date_time_closed - report.date_time_accepted
            # downtime_minutes теперь содержит разницу во времени между завершением и началом работ
            # Можете сохранить значение в минутах или в нужном вам формате
            report.simple = int(downtime.total_seconds() / 60)
            report.save()

        return super().form_valid(form)

    def form_invalid(self, form: CreateMalfunctionsForm):
        print("что-то не так!")
        # Добавьте здесь необходимые действия для обработки невалидной формы
        errors = form.errors.as_data()
        print(errors)
        # Теперь переменная errors содержит информацию о том,
        # почему форма невалидна
        return self.render_to_response(
            self.get_context_data(form=form, errors=errors)
        )
