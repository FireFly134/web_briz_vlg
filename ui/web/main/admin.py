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


class RoutersAdmin(admin.ModelAdmin):
    list_display = (
        "emai",
        "name_router",
    )
    list_display_links = ("emai",)
    search_fields = ("emai",)
    filter = ("emai",)


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
