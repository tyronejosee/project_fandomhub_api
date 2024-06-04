"""ViewSets for News App."""

from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin
from apps.utils.permissions import IsStaffOrReadOnly
from .models import New
from .serializers import NewSerializer, NewListSerializer
from .schemas import new_schemas


@extend_schema_view(**new_schemas)
class NewViewSet(ListCacheMixin, ReadOnlyModelViewSet):
    """
    ViewSet for managing New instances.

    Endpoints:
    - GET /api/v1/news/
    - GET /api/v1/news/{id}/
    """

    permission_classes = [IsStaffOrReadOnly]
    serializer_class = NewSerializer
    search_fields = ["title", "author__username"]
    ordering_fields = ["title", "created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return New.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return NewListSerializer
        return super().get_serializer_class()
