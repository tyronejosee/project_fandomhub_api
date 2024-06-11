"""Views for Playlists App."""

from django.urls import path

from .views import AnimeListView, AnimeListItemView, AnimeListItemDetailView


urlpatterns = [
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
]
