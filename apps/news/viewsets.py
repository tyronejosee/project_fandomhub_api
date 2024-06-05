"""ViewSets for News App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin
from apps.users.permissions import IsModerator
from .models import News
from .serializers import NewsReadSerializer, NewsWriteSerializer, NewsMinimalSerializer
from .schemas import news_schemas


@extend_schema_view(**news_schemas)
class NewsViewSet(ListCacheMixin, ModelViewSet):
    """
    ViewSet for managing News instances.

    Endpoints:
    - GET /api/v1/news/
    - POST /api/v1/news/
    - GET /api/v1/news/{id}/
    - PUT /api/v1/news/{id}/
    - PATCH /api/v1/news/{id}/
    - DELETE /api/v1/news/{id}/
    """

    permission_classes = [IsModerator]
    serializer_class = NewsWriteSerializer
    search_fields = ["name", "author__username"]
    ordering_fields = ["name", "created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return News.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return NewsMinimalSerializer
        elif self.action == "retrieve":
            return NewsReadSerializer
        return super().get_serializer_class()
