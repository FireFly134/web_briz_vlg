from datetime import datetime, timedelta
from typing import Any

from django import forms
from datetime import time


from .models import ModelMalfunctions

labels_dict: dict[str, str] = {
    "address": "Адрес",
    "num_house": "Номер дома",
    "entrance": "Подъезд",
    "flat_or_tel": "Номер квартиры или телефона",
    "dispatcher": "ФИО диспетчера",
    "date_time_accepted": "Дата и время приема заявки",
    "mechanics": "ФИО механика",
    "date_time_transfer": "Дата передачи заявки механикам",
    "malfunction_and_cause": "Неисправность и причина заявки",
    "date_time_closed": "Дата и время закрытия заявки",
    "simple": "Простой",
    "executor_mechanics": "ФИО исполнителя",
    "description": "Примечания",
    "status": "Статус заявки",
}


class CreateMalfunctionsForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            if (
                field.name != "transfer_of_the_application"
                and field.name != "status"
                and "class" not in field.field.widget.attrs
            ):
                if (
                    field.name != "address"
                    and field.name != "dispatcher"
                    and field.name != "executor_mechanics"
                    and field.name != "mechanics"
                ):
                    field.field.widget.attrs["class"] = "form-control"
                else:
                    field.field.widget.attrs["class"] = "form-control select2"
                if field.name == "date_time_accepted":
                    field.field.widget.attrs[
                        "value"
                    ] = field.field.widget.format_value(datetime.now())
                if field.name == "date_time_transfer":
                    field.field.widget.attrs[
                        "value"
                    ] = field.field.widget.format_value(
                        datetime.now() + timedelta(minutes=5)
                    )

                field.field.required = False

    class Meta:
        model = ModelMalfunctions
        fields = labels_dict.keys()
        labels = labels_dict
        widgets = {
            "date_time_accepted": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "date_time_closed": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "date_time_transfer": forms.DateTimeInput(
                attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
            ),
            "malfunction_and_cause": forms.Textarea(
                attrs={"rows": 5, "cols": 40}
            ),
            "description": forms.Textarea(attrs={"rows": 10, "cols": 40}),
        }


class UpdateModelMalfunctionsForm(CreateMalfunctionsForm):
    pass


class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)

        # Установка начальных значений для полей формы
        now = datetime.now()
        self.fields["start_datetime"].initial = datetime.combine(
            now.date(), time.min
        )
        self.fields["end_datetime"].initial = datetime.combine(
            now.date(), time.max
        )

    start_datetime = forms.DateTimeField(
        label="Начальная дата и время",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        ),
    )
    end_datetime = forms.DateTimeField(
        label="Конечная дата и время",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"
        ),
    )
