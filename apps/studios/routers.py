"""Routers for Studios App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import StudioViewSet


router_v1 = DefaultRouter()
router_v1.register(r"studios", StudioViewSet, basename="studio")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
