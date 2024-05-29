"""Routers for Clubs App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import ClubViewSet


router_v1 = DefaultRouter()
router_v1.register(r"clubs", ClubViewSet, basename="club")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
