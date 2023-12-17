from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),  # go home
    path("accounts/login/", views.user_login, name="login"),  # авторизация
    path("logout/", views.user_logout, name="logout"),  # выход из профиля
    path(
        "address_list/",
        login_required(views.ShowAddressList.as_view()),
        name="address_list",
    ),
    path(
        "dispatcher_list/",
        login_required(views.ShowDispatcherList.as_view()),
        name="dispatcher_list",
    ),
    path(
        "mechanics_list/",
        login_required(views.ShowMechanicsList.as_view()),
        name="mechanics_list",
    ),
    path(
        "routers_list/",
        login_required(views.ShowRoutersList.as_view()),
        name="routers_list",
    ),
    path(
        "simcard_list/",
        login_required(views.ShowSimCardList.as_view()),
        name="simcard_list",
    ),
    # path(
    #     "new_address/",
    #     login_required(views.Address.AddressCreate.as_view()),
    #     name="new_address",
    # ),
    path(
        "edit_address/<int:info_id>",
        login_required(views.AddressUpdate.as_view()),
        name="edit_address",
    ),
    # path("delete_address/<int:info_id>",
    #      views.Address.address_delete,
    #      name="delete_address"),
]
