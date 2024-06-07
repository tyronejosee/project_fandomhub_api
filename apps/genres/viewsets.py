"""ViewSets for Genres App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.pagination import LargeSetPagination
from apps.users.permissions import IsContributor
from apps.animes.models import Anime
from apps.mangas.models import Manga
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from .models import Genre, Theme, Demographic
from .serializers import (
    GenreReadSerializer,
    GenreWriteSerializer,
    ThemeReadSerializer,
    ThemeWriteSerializer,
    DemographicReadSerializer,
    DemographicWriteSerializer,
)
from .schemas import genre_schemas, theme_schemas, demographic_schemas


@extend_schema_view(**genre_schemas)
class GenreViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    permission_classes = [IsContributor]
    serializer_class = GenreWriteSerializer
    pagination_class = LargeSetPagination
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Genre.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return GenreReadSerializer
        return super().get_serializer_class()

    @extend_schema(
        summary="Get Animes for Genre",
        description="Retrieve a list of animes for genre.",
    )
    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="animes",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_animes(self, request, *args, **kwargs):
        """
        Action retrieve animes associated with a genre.

        Endpoints:
        - GET api/v1/genres/{id}/animes/
        """
        genre = self.get_object()

        try:
            animes = Anime.objects.get_by_genre(genre)
            if animes.exists():
                serializer = AnimeMinimalSerializer(animes, many=True)
                return Response(serializer.data)
            return Response(
                {"detail": _("No animes found for this genre.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @extend_schema(
        summary="Get Mangas for Genre", description="Retrieve a manga list for genre."
    )
    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="mangas",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_mangas(self, request, *args, **kwargs):
        """
        Action retrieve mangas associated with a genre.

        Endpoints:
        - GET api/v1/genres/{id}/mangas/
        """
        genre = self.get_object()

        try:
            mangas = Manga.objects.get_by_genre(genre)
            if mangas.exists():
                serializer = MangaMinimalSerializer(mangas, many=True)
                return Response(serializer.data)
            return Response(
                {"detail": _("No mangas found for this genre.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema_view(**theme_schemas)
class ThemeViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    permission_classes = [IsContributor]
    serializer_class = ThemeWriteSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Theme.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ThemeReadSerializer
        return super().get_serializer_class()


@extend_schema_view(**demographic_schemas)
class DemographicViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    permission_classes = [IsContributor]
    serializer_class = DemographicWriteSerializer
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Demographic.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DemographicReadSerializer
        return super().get_serializer_class()
