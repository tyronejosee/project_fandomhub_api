"""Routers for Categories App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.categories.viewsets import (
    UrlViewSet, StudioViewSet, GenreViewSet, SeasonViewSet, DemographicViewSet
)


router_v1 = DefaultRouter()
router_v1.register(r"genres", GenreViewSet, basename="genre")
router_v1.register(r"studios", StudioViewSet, basename="studio")
router_v1.register(r"seasons", SeasonViewSet, basename="season")
router_v1.register(r"demographics", DemographicViewSet, basename="demographic")
router_v1.register(r"urls", UrlViewSet, basename="url")


urlpatterns = [
    path("api/v1/", include(router_v1.urls))
]
