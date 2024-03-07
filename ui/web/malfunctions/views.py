from datetime import datetime, timezone
from typing import Any

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from django_stubs_ext import QuerySetAny

from .forms import (
    CreateMalfunctionsForm,
    UpdateModelMalfunctionsForm,
)
from .models import ModelMalfunctions


class CalculationOfDowntime:
    def __init__(self, filter_model: ModelMalfunctions) -> None:
        self.text_hours: str = str()
        self.text_minutes: str = str()
        self.model = filter_model
        self.dt_closed: datetime = (
            filter_model.date_time_closed
            if filter_model.date_time_closed is not None
            else datetime.now()
        )
        self.dt_accepted: datetime = (
            filter_model.date_time_accepted
            if filter_model.date_time_closed is not None
            else datetime.now()
        )
        return

    def cod(self) -> str:
        if self.dt_closed > self.dt_accepted:
            downtime_sec = (self.dt_closed - self.dt_accepted).total_seconds()
            downtime_min = int(downtime_sec / 60)
            full_hours = int(downtime_min // 60)
            minutes = int(downtime_min - (full_hours * 60))
            if full_hours != 0:
                self.text_hours = f"{full_hours} ч."
            if minutes != 0:
                self.text_minutes = f"{minutes} мин."
            return f"{self.text_hours} {self.text_minutes}"
        else:
            return "ОШИБКА! Время закрытия заявки, раньше её создания."


class MalfunctionsList(ListView):
    model: Any = ModelMalfunctions.objects
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

    def form_valid(self, form: UpdateModelMalfunctionsForm) -> HttpResponse:
        report = form.save(commit=False)

        # Рассчитываем время простоя, если есть время завершения
        if report.date_time_closed:
            report.simple = CalculationOfDowntime(filter_model=report).cod()
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
        info.simple = CalculationOfDowntime(filter_model=info).cod()
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

    def form_valid(self, form: CreateMalfunctionsForm) -> HttpResponse:
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

    def form_invalid(self, form: CreateMalfunctionsForm) -> HttpResponse:
        print("что-то не так!")
        # Добавьте здесь необходимые действия для обработки невалидной формы
        errors = form.errors.as_data()
        print(errors)
        # Теперь переменная errors содержит информацию о том,
        # почему форма невалидна
        return self.render_to_response(
            self.get_context_data(form=form, errors=errors)
        )
