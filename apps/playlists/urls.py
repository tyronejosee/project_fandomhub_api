"""Views for Playlists App."""

from django.urls import path

from .views import MyAnimeListView, MyAnimeListItemsView, MyAnimeListItemsDetailView


urlpatterns = [
    path(
        "api/v1/playlists/myanimelist/",
        MyAnimeListView.as_view(),
    ),
    path(
        "api/v1/playlists/myanimelist/animes/",
        MyAnimeListItemsView.as_view(),
    ),
    path(
        "api/v1/playlists/myanimelist/animes/<uuid:item_id>/",
        MyAnimeListItemsDetailView.as_view(),
    ),
]
