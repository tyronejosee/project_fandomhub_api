"""URLs for Tops App."""

from django.urls import path

from .views import (
    TopAnimeView,
    TopMangaView,
    TopCharacterView,
    TopArtistView,
    TopReviewView,
)


urlpatterns = [
    path(
        "api/v1/top/animes/",
        TopAnimeView.as_view(),
    ),
    path(
        "api/v1/top/mangas/",
        TopMangaView.as_view(),
    ),
    path(
        "api/v1/top/characters/",
        TopCharacterView.as_view(),
    ),
    path(
        "api/v1/top/artists/",
        TopArtistView.as_view(),
    ),
    path(
        "api/v1/top/reviews/",
        TopReviewView.as_view(),
    ),
]
