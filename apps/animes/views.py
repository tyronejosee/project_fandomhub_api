"""Views for Animes App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view

from .models import Anime
from .choices import StatusChoices
from .serializers import AnimeMinimalSerializer
from .filters import AnimeSeasonFilter, SchedulesFilter
from .functions import get_current_season, get_upcoming_season
from .schemas import (
    schedule_schemas,
    season_anime_schemas,
    current_season_anime_schemas,
    upcomming_season_anime_schemas,
)


@extend_schema_view(**schedule_schemas)
class ScheduleView(ListAPIView):
    """
    View with filters for scheduled anime of season.

    Endpoints:
    - GET /api/v1/schedules/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    filterset_class = SchedulesFilter

    def get_queryset(self):
        current_season, current_year = get_current_season()
        return Anime.objects.filter(
            status=StatusChoices.AIRING,
            season=current_season,
            year=current_year,
        )

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema_view(**season_anime_schemas)
class SeasonAnimeView(ListAPIView):
    """
    View to get animes filtered by year and season.

    Endpoints:
    - GET /api/v1/seasons/<int:year>/<str:season>/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    filterset_class = AnimeSeasonFilter

    def get_queryset(self):
        season = str(self.kwargs.get("season")).lower()
        year = int(self.kwargs.get("year"))
        return Anime.objects.get_by_year_and_season(season, year)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No animes found for this season."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


@extend_schema_view(**current_season_anime_schemas)
class CurrentSeasonAnimeView(ListAPIView):
    """
    View to get animes of the current season.

    Endpoint:
    - GET /api/v1/seasons/now/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    filterset_class = AnimeSeasonFilter

    def get_queryset(self):
        season, year = get_current_season()
        return Anime.objects.get_by_year_and_season(season, year)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No animes found for the current season."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


@extend_schema_view(**upcomming_season_anime_schemas)
class UpcomingSeasonAnimeView(ListAPIView):
    """
    View to get animes of the upcoming season.

    Endpoint:
    - GET /api/v1/seasons/upcoming/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer
    filterset_class = AnimeSeasonFilter

    def get_queryset(self):
        season, year = get_upcoming_season()
        return Anime.objects.get_by_year_and_season(season, year)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No animes found for the upcoming season."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)
