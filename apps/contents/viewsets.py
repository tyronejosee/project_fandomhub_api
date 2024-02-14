"""Viewsets for Contents App."""

from django.utils.translation import gettext as _
from rest_framework import viewsets
from apps.utils.mixins import LogicalDeleteMixin
from apps.contents.models import Anime, Manga
from apps.contents.serializers import AnimeSerializer, MangaSerializer
from apps.utils.permissions import IsStaffOrReadOnly


class AnimeViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Anime instances.
    """
    serializer_class = AnimeSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name', 'studio_id__name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Anime.objects.filter(available=True)


class MangaViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Manga instances.
    """
    serializer_class = MangaSerializer
    permission_classes = [IsStaffOrReadOnly]
    search_fields = ['name',]
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Manga.objects.filter(available=True)
