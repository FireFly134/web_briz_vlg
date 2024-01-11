from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),  # go home
    path("accounts/login/", views.user_login, name="login"),  # авторизация
    path("logout/", views.user_logout, name="logout"),  # выход из профиля
    # #########################################################################
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
    # #########################################################################
    path(
        "new_address/",
        login_required(views.AddressCreate.as_view()),
        name="new_address",
    ),
    path(
        "new_dispatcher/",
        login_required(views.DispatcherCreate.as_view()),
        name="new_dispatcher",
    ),
    path(
        "new_mechanics/",
        login_required(views.MechanicsCreate.as_view()),
        name="new_mechanics",
    ),
    path(
        "new_routers/",
        login_required(views.RoutersCreate.as_view()),
        name="new_routers",
    ),
    path(
        "new_simcard/",
        login_required(views.SimCardCreate.as_view()),
        name="new_simcard",
    ),
    # #########################################################################
    path(
        "edit_address/<int:info_id>",
        login_required(views.AddressUpdate.as_view()),
        name="edit_address",
    ),
    path(
        "edit_dispatcher/<int:info_id>",
        login_required(views.DispatcherUpdate.as_view()),
        name="edit_dispatcher",
    ),
    path(
        "edit_mechanics/<int:info_id>",
        login_required(views.MechanicsUpdate.as_view()),
        name="edit_mechanics",
    ),
    path(
        "edit_routers/<int:info_id>",
        login_required(views.RoutersUpdate.as_view()),
        name="edit_routers",
    ),
    path(
        "edit_simcard/<int:info_id>",
        login_required(views.SimCardUpdate.as_view()),
        name="edit_simcard",
    ),
    # #########################################################################
    path(
        "address_delete/<int:info_id>",
        views.address_delete,
        name="address_delete",
    ),
    path(
        "dispatcher_delete/<int:info_id>",
        views.dispatcher_delete,
        name="dispatcher_delete",
    ),
    path(
        "mechanics_delete/<int:info_id>",
        views.mechanics_delete,
        name="mechanics_delete",
    ),
    path(
        "routers_delete/<int:info_id>",
        views.routers_delete,
        name="routers_delete",
    ),
    path(
        "simcard_delete/<int:info_id>",
        views.simcard_delete,
        name="simcard_delete",
    ),
]
