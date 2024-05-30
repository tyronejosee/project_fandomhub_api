"""Routers for Animes App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import AnimeViewSet


router = DefaultRouter()
router.register(r"animes", AnimeViewSet, basename="anime")

urlpatterns = [path("api/v1/", include(router.urls))]
