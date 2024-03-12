from django.contrib import admin

from malfunctions.models import ModelMalfunctions


class ModelMalfunctionsAdmin(admin.ModelAdmin):
    list_display = (
        "address",
        "num_house",
        "entrance",
        "date_time_accepted",
        "status",
    )
    list_display_links = ("address",)
    search_fields = ("address",)
    filter = ("date_time_accepted",)


admin.site.register(ModelMalfunctions, ModelMalfunctionsAdmin)
