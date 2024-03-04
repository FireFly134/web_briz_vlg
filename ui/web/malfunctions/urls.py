from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        login_required(views.MalfunctionsList.as_view()),
        name="list",
    ),
    path(
        "create/",
        login_required(views.MalfunctionsCreate.as_view()),
        name="create",
    ),
    path(
        "edit/<int:info_id>",
        login_required(views.MalfunctionsUpdate.as_view()),
        name="edit",
    ),
    path("delete/<int:info_id>", views.delete_contact, name="delete"),
    path(
        "send_archive/<int:info_id>", views.send_archive, name="send_archive"
    ),
    path("send_black/<int:info_id>", views.send_black, name="send_black"),
]
