"""Views for Animes App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .choices import StatusChoices
from .filters import AnimeSeasonFilter
from .filters import SchedulesFilter
from .functions import get_current_season
from .functions import get_upcoming_season
from .models import Anime
from .serializers import AnimeMinimalSerializer


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
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


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
        year = int(self.kwargs.get("year"))
        season = str(self.kwargs.get("season")).lower()
        return Anime.objects.filter(year=year, season=season)

    # TODO: Add mamager

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
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No animes found for the current season."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)


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
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No animes found for the upcoming season."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)
