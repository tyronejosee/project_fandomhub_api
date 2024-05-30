"""URLs for Randoms App."""

from django.urls import path

from .views import RandomAnimeView, RandomMangaView


urlpatterns = [
    path("api/v1/random/anime/", RandomAnimeView.as_view()),
    path("api/v1/random/manga/", RandomMangaView.as_view()),
    # TODO: Pending implementation
    # path("api/v1/random/character/", RandomcharacterView.as_view()),
    # path("api/v1/random/people/", RandomPeopleView.as_view()),
]
