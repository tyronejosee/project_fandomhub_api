"""Viewsets for Contents App."""

from django.db import transaction
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
# from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.utils.pagination import LargeSetPagination, MediumSetPagination
from apps.contents.models import Anime, Manga
from apps.contents.serializers import AnimeListSerializer, MangaListSerializer
from .models import Studio, Genre, Theme, Season, Demographic
from .serializers import (
    StudioSerializer, GenreSerializer, ThemeSerializer,
    SeasonSerializer, DemographicSerializer
)
from .schemas import (
    studio_schemas, genre_schemas, theme_schemas,
    season_schemas, demographic_schemas
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
    # lookup_field = "slug"

    def get_queryset(self):
        return Studio.objects.filter(
            available=True
        ).defer("available", "created_at", "updated_at")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Get Animes for Studio",
        description="Retrieve a list of animes for studio."
    )
    @action(detail=True, methods=["get"], url_path="animes")
    @method_decorator(cache_page(60 * 60 * 2))
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified studio.
        """
        studio = self.get_object()
        anime_list = Anime.objects.filter(studio=studio)
        if anime_list.exists():
            paginator = LargeSetPagination()
            result_page = paginator.paginate_queryset(anime_list, request)
            serializer = AnimeListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
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
    pagination_class = LargeSetPagination
    search_fields = ["name",]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Genre.objects.filter(
            available=True
        ).only("id", "name", "slug")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Get Animes for Genre",
        description="Retrieve a list of animes for genre."
    )
    @action(detail=True, methods=["get"], url_path="animes")
    @method_decorator(cache_page(60 * 60 * 2))
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified genre.
        """
        genre = self.get_object()
        anime_list = Anime.objects.filter(genres=genre)
        if anime_list.exists():
            paginator = MediumSetPagination()
            result_page = paginator.paginate_queryset(anime_list, request)
            serializer = AnimeListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no animes for this genre.")},
            status=status.HTTP_404_NOT_FOUND
        )

    @extend_schema(
        summary="Get Mangas for Genre",
        description="Retrieve a list of mangas for genre."
    )
    @action(detail=True, methods=["get"], url_path="mangas")
    @method_decorator(cache_page(60 * 60 * 2))
    def manga_list(self, request, pk=None):
        """
        Retrieve a list of mangas for the specified genre.
        """
        genre = self.get_object()
        manga_list = Manga.objects.filter(genres=genre)
        if manga_list.exists():
            paginator = MediumSetPagination()
            result_page = paginator.paginate_queryset(manga_list, request)
            serializer = MangaListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no mangas for this genre.")},
            status=status.HTTP_404_NOT_FOUND
        )


@extend_schema_view(**theme_schemas)
class ThemeViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Theme instances.
    """
    serializer_class = ThemeSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name",]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Theme.objects.filter(
            available=True
        ).only("id", "name", "slug")

    @method_decorator(cache_page(60 * 60 * 2, key_prefix="theme_list"))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        cache.clear()
        return super().create(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


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
        return Season.objects.filter(
            available=True
        ).only("id", "season", "year", "fullname")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @action(detail=True, methods=["get"], url_path="animes")
    @method_decorator(cache_page(60 * 60 * 2))
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified season.
        """
        season = self.get_object()
        anime_list = Anime.objects.filter(season=season)
        if anime_list.exists():
            paginator = MediumSetPagination()
            result_page = paginator.paginate_queryset(anime_list, request)
            serializer = AnimeListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no animes for this season.")},
            status=status.HTTP_404_NOT_FOUND
        )


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
        return Demographic.objects.filter(
            available=True
        ).values("id", "name")

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
