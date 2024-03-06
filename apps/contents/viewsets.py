"""Viewsets for Contents App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.utils.mixins import LogicalDeleteMixin
from apps.contents.models import Anime, Manga
from apps.contents.serializers import (
    AnimeSerializer, MangaSerializer, AnimeListSerializer
)
from apps.utils.permissions import IsStaffOrReadOnly
from apps.contents.schemas import anime_schemas, manga_schemas


@extend_schema_view(**anime_schemas)
class AnimeViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Anime instances.
    """
    serializer_class = AnimeSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name", "studio__name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Anime.objects.filter(available=True)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Get Popular Animes",
        description="Retrieve a list of the 50 most popular anime."
    )
    @action(detail=False, methods=["get"], url_path="populars")
    @method_decorator(cache_page(60 * 60 * 2))
    def popular_list(self, request, pk=None):
        """
        Action return a list of the 50 most popular anime.
        """
        popular_list = Anime.objects.order_by("-popularity")[:50]
        if not popular_list:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AnimeListSerializer(popular_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(**manga_schemas)
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

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
