import os
from typing import Any, Dict

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import (
    HttpRequest,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from django_stubs_ext import QuerySetAny

from .forms import (
    CreateMalfunctionsForm,
    UpdateModelMalfunctionsForm,
)
from .models import ModelMalfunctions


class MalfunctionsList(ListView):
    model = ModelMalfunctions
    template_name = "malfunctions/list.html"
    context_object_name = "list"

    def get_queryset(
        self,
    ) -> QuerySetAny[ModelMalfunctions, ModelMalfunctions]:
        return ModelMalfunctions.objects.all()


class MalfunctionsUpdate(
    UpdateView,
):
    model = ModelMalfunctions
    form_class = UpdateModelMalfunctionsForm
    template_name = "malfunctions/edit.html"
    pk_url_kwarg = "info_id"
    context_object_name = "info"
    success_url = reverse_lazy("list")


@login_required
def delete_contact(
    request: HttpRequest, info_id: int
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    info = ModelMalfunctions.objects.get(pk=info_id)
    if request.user.is_superuser:
        info.delete()
        return redirect("list")
    raise PermissionDenied()


class MalfunctionsCreate(
    CreateView
):
    model = ModelMalfunctions
    form_class = CreateMalfunctionsForm
    template_name = "malfunctions/create.html"
    success_url = reverse_lazy("create")

    def form_valid(
        self,
        form: CreateMalfunctionsForm,
    ) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        report = form.save(commit=False)
        report.save()

        return redirect("list")
