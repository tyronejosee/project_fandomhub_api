"""Routers for Profiles App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import ProfileViewSet

# /(?P<id>\d+)

router_v1 = DefaultRouter()
router_v1.register(r"profiles", ProfileViewSet, basename="profile")

urlpatterns = [
    path("api/v1/", include(router_v1.urls))
]
