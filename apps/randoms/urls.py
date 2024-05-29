"""URLs for Randoms App."""

from django.urls import path

from .views import RandomAnimeView


urlpatterns = [
    path("api/v1/random/anime/", RandomAnimeView.as_view()),
]
