"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import Any

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from malfunctions.views import MalfunctionsAPIView
from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL


urlpatterns: list[Any] = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("malfunctions/", include("malfunctions.urls")),
    path(
        "api/v1/malfunctions",
        MalfunctionsAPIView.as_view(),
        name="m_API"
    )
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
