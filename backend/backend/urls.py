from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.http import JsonResponse


def root_view(request):
    return JsonResponse({
        "message": "👋 Welcome to the Django backend!",
        "status": "OK"
    })


urlpatterns = [
    path("", root_view),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls", namespace="core")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
