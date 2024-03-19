from django import forms
from django.contrib import admin

from main.models import (
    AddressList,
    DispatcherList,
    MechanicsList,
    Routers,
    SimCard,
)


class AddressListAdmin(admin.ModelAdmin):
    list_display = ("address",)
    list_display_links = ("address",)
    search_fields = ("address",)
    filter = ("address",)


class DispatcherListAdmin(admin.ModelAdmin):
    list_display = ("fio",)
    list_display_links = ("fio",)
    search_fields = ("fio",)
    filter = ("fio",)


class MechanicsListAdmin(admin.ModelAdmin):
    list_display = ("fio",)
    list_display_links = ("fio",)
    search_fields = ("fio",)
    filter = ("fio",)


class RouterAdminForm(forms.ModelForm):
    class Meta:
        model = Routers
        exclude = []

    def __init__(self, *args, **kwargs):
        super(RouterAdminForm, self).__init__(*args, **kwargs)
        # Получаем список уже выбранных сим-карт для других роутеров
        selected_sim_cards = Routers.objects.exclude(
            sim_card=None
        ).values_list("sim_card__id", flat=True)

        # Если редактируемый роутер уже имеет связанную сим-карту,
        # добавляем её в список выбранных для исключения из выбора
        if self.instance.sim_card:
            selected_sim_cards = selected_sim_cards.exclude(
                sim_card_id=self.instance.sim_card.id
            )

        # Исключаем выбранные сим-карты из списка доступных
        self.fields["sim_card"].queryset = SimCard.objects.exclude(
            id__in=selected_sim_cards
        )


class RoutersAdmin(admin.ModelAdmin):
    form = RouterAdminForm
    list_display = (
        "imei",
        "name_router",
        "sim_card",
        "info_install",
    )
    list_display_links = ("imei",)
    search_fields = ("imei",)
    filter = ("imei",)


class SimCardAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "ip",
        "operator_name",
    )
    list_display_links = ("phone_number",)
    search_fields = (
        "phone_number",
        "ip",
        "operator_name",
    )
    filter = (
        "phone_number",
        "ip",
        "operator_name",
    )


admin.site.register(AddressList, AddressListAdmin)
admin.site.register(DispatcherList, DispatcherListAdmin)
admin.site.register(MechanicsList, MechanicsListAdmin)
admin.site.register(Routers, RoutersAdmin)
admin.site.register(SimCard, SimCardAdmin)
