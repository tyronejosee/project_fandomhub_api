"""ViewSets for News App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema_view

from apps.utils.permissions import IsStaffOrReadOnly
from .models import New
from .serializers import NewSerializer, NewListSerializer
from .schemas import new_schemas


@extend_schema_view(**new_schemas)
class NewViewSet(ReadOnlyModelViewSet):
    """
    ViewSet for managing New instances.

    Endpoints:
    - GET /api/v1/news/
    - GET /api/v1/news/{id}/
    """

    serializer_class = NewSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["title", "author__username"]
    ordering_fields = ["title", "created_at"]
    ordering = ["id"]

    def get_queryset(self):
        return New.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return NewListSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
