"""Routers for Playlists App."""

from django.urls import path

from .views import PlaylistAPIView, PlaylistAnimeAPIView


urlpatterns = [
    path("api/v1/playlists/me/", PlaylistAPIView.as_view()),
    path("api/v1/playlists/animes/", PlaylistAnimeAPIView.as_view()),
    path("api/v1/playlists/animes/<uuid:pk>/", PlaylistAnimeAPIView.as_view()),
]
