"""ViewSets for Seasons App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.pagination import MediumSetPagination
from apps.users.permissions import IsContributor
from apps.animes.models import Anime
from apps.animes.serializers import AnimeMinimalSerializer
from .models import Season
from .serializers import SeasonReadSerializer, SeasonWriteSerializer
from .schemas import season_schemas


@extend_schema_view(**season_schemas)
class SeasonViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    serializer_class = SeasonWriteSerializer
    permission_classes = [IsContributor]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_queryset(self):
        return Season.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return SeasonReadSerializer
        return super().get_serializer_class()

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
        Action retrieve animes associated with a season.

        Endpoints:
        - GET /api/v1/seasons/{id}/animes/
        """
        season = self.get_object()

        try:
            animes = Anime.objects.get_by_season(season)
            if animes.exists():
                paginator = MediumSetPagination()
                result_page = paginator.paginate_queryset(animes, request)
                serializer = AnimeMinimalSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            return Response(
                {"detail": _("No animes found for this season.")},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
