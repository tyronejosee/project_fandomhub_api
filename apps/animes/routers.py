"""Routers for Animes App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import AnimeViewSet
from .views import SeasonAnimeView, CurrentSeasonAnimeView, UpcomingSeasonAnimeView


router = DefaultRouter()
router.register(r"animes", AnimeViewSet, basename="anime")

urlpatterns = [
    path(
        "api/v1/",
        include(router.urls),
    ),
    path(
        "api/v1/seasons/<int:year>/<str:season>/",
        SeasonAnimeView.as_view(),
    ),
    path(
        "api/v1/seasons/now/",
        CurrentSeasonAnimeView.as_view(),
    ),
    path(
        "api/v1/seasons/upcoming/",
        UpcomingSeasonAnimeView.as_view(),
    ),
]
