"""Views for Playlists App."""

from django.urls import path

from .views import (
    AnimeListView,
    AnimeListItemView,
    AnimeListItemDetailView,
    MangaListView,
    MangaListItemView,
    MangaListItemDetailView,
    MangaListExportView,
)


urlpatterns = [
    # Animelist urls
    path(
        "api/v1/playlists/animelist/",
        AnimeListView.as_view(),
    ),
    path(
        "api/v1/playlists/animelist/animes/",
        AnimeListItemView.as_view(),
    ),
    path(
        "api/v1/playlists/animelist/animes/<uuid:item_id>/",
        AnimeListItemDetailView.as_view(),
    ),
    # Mangalist urls
    path(
        "api/v1/playlists/mangalist/",
        MangaListView.as_view(),
    ),
    path(
        "api/v1/playlists/mangalist/mangas/",
        MangaListItemView.as_view(),
    ),
    path(
        "api/v1/playlists/mangalist/mangas/<uuid:item_id>/",
        MangaListItemDetailView.as_view(),
    ),
    path(
        "api/v1/playlists/mangalist/export/",
        MangaListExportView.as_view(),
    ),
]
