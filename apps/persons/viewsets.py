"""Viewsets for Persons App."""

from rest_framework import viewsets
from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.permissions import IsStaffOrReadOnly
from apps.persons.models import Author
from apps.persons.serializers import AuthorSerializer


class AuthorViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Author instances.
    """
    serializer_class = AuthorSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Author.objects.filter(available=True)
