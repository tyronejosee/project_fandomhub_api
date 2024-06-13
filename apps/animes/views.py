"""Views for Animes App."""

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Anime
from .functions import get_current_season, get_upcoming_season
from .serializers import AnimeMinimalSerializer


class SeasonAnimeView(ListAPIView):
    """
    View to get animes filtered by year and season.

    Endpoints:
    - GET /api/v1/seasons/<int:year>/<str:season>/
    """

    permission_classes = [AllowAny]
    serializer_class = AnimeMinimalSerializer

    def get_queryset(self):
        year = int(self.kwargs.get("year"))
        season = str(self.kwargs.get("season")).lower()
        return Anime.objects.filter(year=year, season=season)

    # TODO: Add mamager

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

    def get_queryset(self):
        season, year = get_current_season()
        return Anime.objects.get_by_year_and_season(season, year)

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

    def get_queryset(self):
        season, year = get_upcoming_season()
        return Anime.objects.get_by_year_and_season(season, year)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response(
                {"detail": "No animes found for the upcoming season."},
                status=status.HTTP_404_NOT_FOUND,
            )
        return super().list(request, *args, **kwargs)
