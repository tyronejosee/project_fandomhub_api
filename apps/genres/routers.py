"""Routers for Genres App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import GenreViewSet


router_v1 = DefaultRouter()
router_v1.register(r"genres", GenreViewSet, basename="genre")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
