"""Routers for Animes App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrentSeasonAnimeView
from .views import ScheduleView
from .views import SeasonAnimeView
from .views import UpcomingSeasonAnimeView
from .viewsets import AnimeViewSet

router = DefaultRouter()
router.register(r"animes", AnimeViewSet, basename="anime")

urlpatterns = [
    path(
        "api/v1/",
        include(router.urls),
    ),
    path(
        "api/v1/schedules/",
        ScheduleView.as_view(),
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
