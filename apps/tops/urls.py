"""URLs for Tops App."""

from django.urls import path

from .views import TopAnimeView


urlpatterns = [
    path(
        "api/v1/top/animes/",
        TopAnimeView.as_view(),
    ),
]
