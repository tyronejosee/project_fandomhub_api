"""URLs for Recommendations App."""

from django.urls import path

from .views import AnimeRecommendationView, MangaRecommendationView


urlpatterns = [
    path(
        "api/v1/recommendations/anime/",
        AnimeRecommendationView.as_view(),
    ),
    path(
        "api/v1/recommendations/manga/",
        MangaRecommendationView.as_view(),
    ),
]
