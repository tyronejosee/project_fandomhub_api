"""Routers for Mangas App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import MangaViewSet


router = DefaultRouter()
router.register(r"mangas", MangaViewSet, basename="manga")

urlpatterns = [path("api/v1/", include(router.urls))]
