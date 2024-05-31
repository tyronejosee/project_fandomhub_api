"""Routers for Categories App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import ThemeViewSet, DemographicViewSet


router_v1 = DefaultRouter()
router_v1.register(r"themes", ThemeViewSet, basename="theme")
router_v1.register(r"demographics", DemographicViewSet, basename="demographic")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
