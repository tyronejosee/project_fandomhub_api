"""Routers for Playlists App."""

from django.urls import path

from .views import PlaylistAPIView, PlaylistAnimeAPIView, PlaylistMangaAPIView, PlaylistAnimeDetailView


urlpatterns = [
    path("api/v1/playlists/me/", PlaylistAPIView.as_view()),
    path("api/v1/playlists/animes/", PlaylistAnimeAPIView.as_view()),
    path("api/v1/playlists/animes/<uuid:item_id>/",
         PlaylistAnimeDetailView.as_view()),
    path("api/v1/playlists/mangas/", PlaylistMangaAPIView.as_view()),
    path("api/v1/playlists/mangas/<uuid:pk>/", PlaylistMangaAPIView.as_view()),
]
