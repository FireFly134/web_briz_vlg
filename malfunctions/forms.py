from typing import Any

from django import forms

from .models import ModelMalfunctions

labels_dict: dict[str, str] = {
    "address": "Адрес",
    "num_house": "Номер дома",
    "entrance": "Подъезд",
    "flat_or_tel": "Номер квартины или телефона",
    "dispatcher": "ФИО диспетчера",
    "date_time_accepted": "Дата и время приема заявки",
    "mechanics": "ФИО механика",
    "date_time_closed": "Дата и время закрытия заявки",
    "malfunction_and_cause": "Неисправность и причина заявки",
    "transfer_of_the_application": "Передача по смене",
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
                attrs={"type": "datetime-local"}
            ),
            "malfunction_and_cause": forms.Textarea(
                attrs={"rows": 5, "cols": 40}
            ),
            "description": forms.Textarea(attrs={"rows": 10, "cols": 40}),
        }


class UpdateModelMalfunctionsForm(CreateMalfunctionsForm):
    pass
