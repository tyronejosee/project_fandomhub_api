"""Viewsets for Contents App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.pagination import LargeSetPagination, MediumSetPagination
from apps.users.permissions import IsContributor
from apps.contents.models import Anime, Manga
from apps.contents.serializers import AnimeMinimalSerializer, MangaMinimalSerializer
from .models import Studio, Genre, Theme, Season, Demographic
from .serializers import (
    StudioReadSerializer,
    StudioWriteSerializer,
    GenreReadSerializer,
    GenreWriteSerializer,
    ThemeReadSerializer,
    ThemeWriteSerializer,
    SeasonReadSerializer,
    SeasonWriteSerializer,
    DemographicReadSerializer,
    DemographicWriteSerializer,
)
from .schemas import (
    studio_schemas,
    genre_schemas,
    theme_schemas,
    season_schemas,
    demographic_schemas,
)


@extend_schema_view(**studio_schemas)
class StudioViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Studio instances.

    Endpoints:
    - GET /api/v1/studios/
    - POST /api/v1/studios/
    - GET /api/v1/studios/{id}/
    - PUT /api/v1/studios/{id}/
    - PATCH /api/v1/studios/{id}/
    - DELETE /api/v1/studios/{id}/
    """

    serializer_class = StudioReadSerializer
    permission_classes = [IsContributor]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Studio.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return StudioWriteSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Animes for Studio",
        description="Retrieve a list of animes for studio.",
    )
    @action(detail=True, methods=["get"], url_path="animes")
    @method_decorator(cache_page(60 * 60 * 2))
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified studio.

        Endpoints:
        - GET /api/v1/studios/{id}/animes/
        """
        studio = self.get_object()
        anime_list = Anime.objects.filter(studio=studio)
        if anime_list.exists():
            paginator = LargeSetPagination()
            result_page = paginator.paginate_queryset(anime_list, request)
            serializer = AnimeMinimalSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no animes for this studio.")},
            status=status.HTTP_404_NOT_FOUND,
        )


@extend_schema_view(**genre_schemas)
class GenreViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Genre instances.

    Endpoints:
    - GET /api/v1/genres/
    - POST /api/v1/genres/
    - GET /api/v1/genres/{id}/
    - PUT /api/v1/genres/{id}/
    - PATCH /api/v1/genres/{id}/
    - DELETE /api/v1/genres/{id}/
    """

    serializer_class = GenreReadSerializer
    permission_classes = [IsContributor]
    pagination_class = LargeSetPagination
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Genre.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return GenreWriteSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Get Animes for Genre",
        description="Retrieve a list of animes for genre.",
    )
    @action(detail=True, methods=["get"], url_path="animes")
    @method_decorator(cache_page(60 * 60 * 2))
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified genre.

        Endpoints:
        - GET /api/v1/genres/{id}/animes/
        """
        genre = self.get_object()
        anime_list = Anime.objects.filter(genres=genre)
        if anime_list.exists():
            paginator = MediumSetPagination()
            result_page = paginator.paginate_queryset(anime_list, request)
            serializer = AnimeMinimalSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no animes for this genre.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @extend_schema(
        summary="Get Mangas for Genre", description="Retrieve a manga list for genre."
    )
    @action(detail=True, methods=["get"], url_path="mangas")
    @method_decorator(cache_page(60 * 60 * 2))
    def manga_list(self, request, pk=None):
        """
        Retrieve a manga list for the specified genre.

        Endpoints:
        - GET /api/v1/studios/{id}/mangas/
        """
        genre = self.get_object()
        manga_list = Manga.objects.filter(genres=genre)
        if manga_list.exists():
            paginator = MediumSetPagination()
            result_page = paginator.paginate_queryset(manga_list, request)
            serializer = MangaMinimalSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no mangas for this genre.")},
            status=status.HTTP_404_NOT_FOUND,
        )


@extend_schema_view(**theme_schemas)
class ThemeViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Theme instances.

    Endpoints:
    - GET /api/v1/themes/
    - POST /api/v1/themes/
    - GET /api/v1/themes/{id}/
    - PUT /api/v1/themes/{id}/
    - PATCH /api/v1/themes/{id}/
    - DELETE /api/v1/themes/{id}/
    """

    serializer_class = ThemeReadSerializer
    permission_classes = [IsContributor]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Theme.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ThemeWriteSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


@extend_schema_view(**season_schemas)
class SeasonViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Season instances.

    Endpoints:
    - GET /api/v1/seasons/
    - POST /api/v1/seasons/
    - GET /api/v1/seasons/{id}/
    - PUT /api/v1/seasons/{id}/
    - PATCH /api/v1/seasons/{id}/
    - DELETE /api/v1/seasons/{id}/
    """

    serializer_class = SeasonReadSerializer
    permission_classes = [IsContributor]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Season.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return SeasonWriteSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=["get"], url_path="animes")
    @method_decorator(cache_page(60 * 60 * 2))
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified season.

        Endpoints:
        - GET /api/v1/seasons/{id}/animes/
        """
        season = self.get_object()
        anime_list = Anime.objects.filter(season=season)
        if anime_list.exists():
            paginator = MediumSetPagination()
            result_page = paginator.paginate_queryset(anime_list, request)
            serializer = AnimeMinimalSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no animes for this season.")},
            status=status.HTTP_404_NOT_FOUND,
        )


@extend_schema_view(**demographic_schemas)
class DemographicViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Demographic instances.

    Endpoints:
    - GET /api/v1/demographics/
    - POST /api/v1/demographics/
    - GET /api/v1/demographics/{id}/
    - PUT /api/v1/demographics/{id}/
    - PATCH /api/v1/demographics/{id}/
    - DELETE /api/v1/demographics/{id}/
    """

    serializer_class = DemographicReadSerializer
    permission_classes = [IsContributor]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Demographic.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DemographicWriteSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
