"""Routers for News App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import NewsViewSet


router_v1 = DefaultRouter()
router_v1.register(r"news", NewsViewSet, basename="news")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
