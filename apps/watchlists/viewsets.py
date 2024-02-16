"""Viewsets for Watchlists App."""

from rest_framework import viewsets
from apps.watchlists.models import AnimeWatchlist, MangaWatchlist
from apps.watchlists.serializers import (
    AnimeWatchlistSerializer, MangaWatchlistSerializer
)


class AnimeWatchlistViewSet(viewsets.ModelViewSet):
    """
    Pending.
    """
    serializer_class = AnimeWatchlistSerializer
    search_fields = ['user', 'anime__name']
    ordering_fields = ['user']
    ordering = ['id']

    def get_queryset(self):
        return AnimeWatchlist.objects.all()


class MangaWatchlistViewSet(viewsets.ModelViewSet):
    """
    Pending.
    """
    serializer_class = MangaWatchlistSerializer
    search_fields = ['user', 'manga__name']
    ordering_fields = ['user']
    ordering = ['id']

    def get_queryset(self):
        return MangaWatchlist.objects.all()
