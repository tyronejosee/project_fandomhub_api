"""Viewsets for Contents App."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.utils.mixins import LogicalDeleteMixin
from apps.contents.models import Anime, Manga
from apps.contents.serializers import (
    AnimeSerializer, MangaSerializer, AnimeListSerializer
)
from apps.utils.permissions import IsStaffOrReadOnly
from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.contents.schemas import anime_schemas


@extend_schema_view(**anime_schemas)
class AnimeViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Anime instances.
    """
    serializer_class = AnimeSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name", "studio_id__name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Anime.objects.filter(available=True)

    @extend_schema(
        summary="Get Popular Animes",
        description="Retrieve a list of the 50 most popular anime."
    )
    @action(detail=False, methods=["get"], url_path="populars")
    def popular_list(self, request, pk=None):
        """
        Action return a list of the 50 most popular anime.
        """
        popular_list = Anime.objects.order_by("-popularity")[:50]
        if not popular_list:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AnimeListSerializer(popular_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MangaViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Manga instances.
    """
    serializer_class = MangaSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name",]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Manga.objects.filter(available=True)
