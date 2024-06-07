"""Viewsets for Categories App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.users.permissions import IsContributor
from .models import Theme, Demographic
from .serializers import (
    ThemeReadSerializer,
    ThemeWriteSerializer,
    DemographicReadSerializer,
    DemographicWriteSerializer,
)
from .schemas import theme_schemas, demographic_schemas


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
