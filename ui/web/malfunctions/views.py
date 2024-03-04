from datetime import datetime, timezone

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
    model = ModelMalfunctions.objects
    template_name = "malfunctions/list.html"
    context_object_name = "list"

    def get_queryset(
        self,
    ) -> QuerySetAny[ModelMalfunctions, ModelMalfunctions]:
        return ModelMalfunctions.objects.all().order_by("-date_time_accepted")


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
            downtime_sec = report.date_time_closed - report.date_time_accepted
            downtime_min = int(downtime_sec.total_seconds() / 60)
            full_hours = int(downtime_min // 60)
            minutes = downtime_min - (full_hours * 60)
            report.simple = f"{full_hours}ч. {minutes}мин.".strip(
                "0ч. "
            ).strip(" 0мин.")

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
        info.date_time_closed = datetime.now().astimezone(timezone.utc)
        # Рассчитываем время простоя, если есть время завершения
        downtime_sec = (
            info.date_time_closed - info.date_time_accepted
        ).total_seconds()
        downtime_min = int(downtime_sec / 60)
        full_hours = int(downtime_min // 60)
        minutes = downtime_min - (full_hours * 60)
        info.simple = f"{full_hours}ч. {minutes}мин.".strip("0ч. ").strip(
            " 0мин."
        )
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
            # downtime_minutes теперь содержит разницу во времени между
            # завершением и началом работ
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
