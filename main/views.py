import datetime
import json
import os
from typing import Any

from django import forms
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import (
    FileResponse,
    Http404,
    HttpRequest,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render

from .forms import (
    UserLoginForms,
)
from .models import (
    unit,
)
from .services import ExcelReportGenerator


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")
