from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import (
    accounting_for_purchased_equipment,
    accounting_of_services_and_equipment,
    accounting_of_services_and_equipment_description,
    details,
)


class UserLoginForms(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class accounting_for_purchased_equipment_form(
    forms.ModelForm[accounting_for_purchased_equipment]
):
    name = forms.CharField(
        label="Наименование покупного оборудования",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = accounting_for_purchased_equipment
        fields = ("name",)


class accounting_of_services_and_equipment_form(
    forms.ModelForm[accounting_of_services_and_equipment]
):
    name = forms.CharField(
        label="Наименование услуг или оборудования",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = accounting_of_services_and_equipment
        fields = ("name",)


class accounting_of_services_and_equipment_description_form(
    forms.ModelForm[accounting_of_services_and_equipment_description]
):
    description = forms.CharField(
        label="Расшифровка услуг или оборудования",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    services = forms.ModelMultipleChoiceField(
        queryset=accounting_of_services_and_equipment.objects.all(),
        label="Наименование услуг или оборудования",
    )

    class Meta:
        model = accounting_of_services_and_equipment_description
        exclude = (
            "description",
            "services",
        )


class details_form(forms.ModelForm[details]):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control select2"

    class Meta:
        model = details
        fields = (
            "name",
            "link",
        )
        labels = ("Наименование детали", "Ссылка на деталь")
        widgets = {
            "name": forms.Select(
                attrs={"id": "id_choice_id", "style": "width:50%"}
            ),
            "link": forms.TextInput(attrs={"style": "width:50%"}),
        }
