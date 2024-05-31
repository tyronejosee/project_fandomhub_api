"""Routers for Characters App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import CharacterViewSet


router_v1 = DefaultRouter()
router_v1.register(r"characters", CharacterViewSet, basename="character")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
