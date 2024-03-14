"""Routers for Playlists App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.playlists.viewsets import (
    PlaylistViewSet, PlaylistAnimeViewSet, PlaylistMangaViewSet
)

router_v1 = DefaultRouter()
router_v1.register(r"playlists", PlaylistViewSet, basename="playlist")
router_v1.register(r"playlist-anime", PlaylistAnimeViewSet, basename="p-anime")
router_v1.register(r"playlist-manga", PlaylistMangaViewSet, basename="p-anime")

urlpatterns = [
    path("api/v1/", include(router_v1.urls))
]
