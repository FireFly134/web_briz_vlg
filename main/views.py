import datetime
import json
import os
from typing import Any

from django import forms
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render

from .forms import (
    UserLoginForms,
)


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def user_login(
    request: HttpRequest, next_page: str = "home"
) -> HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect:
    if request.method == "POST":
        form = UserLoginForms(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(request.POST.get("login_next", ""))
    else:
        form = UserLoginForms()
        next_page = (
            request.GET.get("next", "")
            if request.GET.get("next") is not None
            else "home"
        )
    return render(
        request,
        "main/login.html",
        context={"form": form, "next_page": next_page},
    )


def user_logout(
    request: HttpRequest,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    logout(request)
    return redirect("home")
