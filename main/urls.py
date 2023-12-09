from django.conf import urls
from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="home"),  # go home
    path("accounts/login/", views.user_login, name="login"),  # авторизация
    path("logout/", views.user_logout, name="logout"),  # выход из профиля
]
