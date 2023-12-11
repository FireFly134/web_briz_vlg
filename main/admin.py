from django.contrib import admin

from main.models import (
    AddressList,
    DispatcherList,
    MechanicsList,
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


admin.site.register(AddressList, AddressListAdmin)
admin.site.register(DispatcherList, DispatcherListAdmin)
admin.site.register(MechanicsList, MechanicsListAdmin)
