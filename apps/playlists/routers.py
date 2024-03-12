"""Routers for Playlists App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.playlists.views import PlaylistViewSet

router_v1 = DefaultRouter()
router_v1.register(r"playlists", PlaylistViewSet, basename="playlist")

urlpatterns = [
    path("api/v1/", include(router_v1.urls))
]
