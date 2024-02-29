"""Viewsets for Contents App."""

from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.contents.models import Anime
from apps.contents.serializers import AnimeSerializer
from apps.categories.models import Studio, Genre, Season, Demographic
from apps.categories.serializers import (
    StudioSerializer, GenreSerializer, SeasonSerializer, DemographicSerializer
)
from apps.categories.schemas import (
    studio_schemas, genre_schemas, season_schemas, demographic_schemas
)


@extend_schema_view(**studio_schemas)
class StudioViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Studio instances.
    """
    serializer_class = StudioSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Studio.objects.filter(available=True)

    @extend_schema(
        summary="Get Animes for Studio",
        description="Retrieve a list of animes for studio."
    )
    @action(detail=True, methods=["get"], url_path="animes")
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified studio.
        """
        studio = self.get_object()
        anime_list = Anime.objects.filter(studio_id=studio)
        if anime_list.exists():
            serializer = AnimeSerializer(anime_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": _("There are no animes for this studio.")},
            status=status.HTTP_404_NOT_FOUND
        )


@extend_schema_view(**genre_schemas)
class GenreViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Genre instances.
    """
    serializer_class = GenreSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name",]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Genre.objects.filter(available=True)

    @extend_schema(
        summary="Get Animes for Genre",
        description="Retrieve a list of animes for genre."
    )
    @action(detail=True, methods=["get"], url_path="animes")
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified genre.
        """
        genre = self.get_object()
        anime_list = Anime.objects.filter(genre_id=genre)
        if anime_list.exists():
            serializer = AnimeSerializer(anime_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": _("There are no animes for this genre.")},
            status=status.HTTP_404_NOT_FOUND
        )


@extend_schema_view(**season_schemas)
class SeasonViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Season instances.
    """
    serializer_class = SeasonSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Season.objects.filter(available=True)


@extend_schema_view(**demographic_schemas)
class DemographicViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Demographic instances.
    """
    serializer_class = DemographicSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Demographic.objects.filter(available=True)
