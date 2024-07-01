"""URLs for Randoms App."""

from django.urls import path

from .views import (
    RandomAnimeView,
    RandomMangaView,
    RandomcharacterView,
    RandomPersonView,
)


urlpatterns = [
    path(
        "api/v1/random/anime/",
        RandomAnimeView.as_view(),
    ),
    path(
        "api/v1/random/manga/",
        RandomMangaView.as_view(),
    ),
    path(
        "api/v1/random/character/",
        RandomcharacterView.as_view(),
    ),
    path(
        "api/v1/random/person/",
        RandomPersonView.as_view(),
    ),
]
