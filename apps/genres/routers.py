"""Routers for Genres App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import GenreViewSet, ThemeViewSet, DemographicViewSet


router_v1 = DefaultRouter()
router_v1.register(r"themes", ThemeViewSet, basename="theme")
router_v1.register(r"demographics", DemographicViewSet, basename="demographic")
router_v1.register(r"genres", GenreViewSet, basename="genre")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
