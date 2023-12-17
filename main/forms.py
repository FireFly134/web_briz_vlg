from typing import Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import (
    AddressList,
    DispatcherList,
    MechanicsList,
    Routers,
    SimCard,
)

simcard_list: dict[str, str] = {
    "phone_number": "Номер телефона",
    "ip": "Статический IP симкарты",
    "operator_name": "Оператор"
                                }
routers_list: dict[str, str] = {
    "name_router": "Название роутера",
    "emai": "EMAI номер роутера",
}


class UserLoginForms(AuthenticationForm):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class AddressListForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            field.field.required = False

    class Meta:
        model = AddressList
        fields = ["address"]
        labels = {"address": "Адрес"}


class DispatcherListForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            field.field.required = False

    class Meta:
        model = DispatcherList
        fields = ["fio"]
        labels = {"fio": "ФИО диспетчера"}


class MechanicsListForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            field.field.required = False

    class Meta:
        model = MechanicsList
        fields = ["fio"]
        labels = {"fio": "ФИО механика"}


class RoutersForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            field.field.required = False

    class Meta:
        model = Routers
        fields = routers_list.keys()
        labels = routers_list


class SimCardForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
            field.field.required = False

    class Meta:
        model = SimCard
        fields = simcard_list.keys()
        labels = simcard_list
