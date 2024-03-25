"""Routers for Playlists App."""

from django.urls import path

from .views import PlaylistAnimeList
from .views import PlaylistList

urlpatterns = [
    path("api/v1/playlists/", PlaylistList.as_view()),
    path("api/v1/playlists/animes/", PlaylistAnimeList.as_view()),
    path("api/v1/playlists/animes/<uuid:pk>/", PlaylistAnimeList.as_view()),
]
