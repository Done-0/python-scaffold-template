"""
URL configuration for python-scaffold-template project.
"""

from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from src.controller.welcome_controller import welcome, error_demo

urlpatterns = [
    # Django 管理后台
    path("admin/", admin.site.urls),
    # API 文档
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # 欢迎和演示接口
    path("", welcome, name="welcome"),
    path("api/error", error_demo, name="error"),
]
