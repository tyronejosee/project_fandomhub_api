"""Viewsets for Persons App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view
from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.persons.models import Author
from apps.persons.serializers import AuthorSerializer
from apps.persons.schemas import author_schemas


@extend_schema_view(**author_schemas)
class AuthorViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Author instances.
    """
    serializer_class = AuthorSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["id"]

    def get_queryset(self):
        return Author.objects.filter(available=True)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
