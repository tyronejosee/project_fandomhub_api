"""Viewsets for Contents App."""

from django.http import Http404
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.mixins import LogicalDeleteMixin
from apps.contents.models import Anime
from apps.contents.serializers import AnimeSerializer
from apps.categories.models import Url, Studio, Genre, Season, Demographic, Author
from apps.categories.serializers import (
    UrlSerializer, StudioSerializer, GenreSerializer, SeasonSerializer,
    DemographicSerializer, AuthorSerializer,
)


class UrlViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Url instances.
    """
    serializer_class = UrlSerializer
    search_fields = ['url', 'tag']
    ordering_fields = ['tag']
    ordering = ['id']

    def get_queryset(self):
        return Url.objects.filter(available=True)


class StudioViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Studio instances.
    """
    serializer_class = StudioSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Studio.objects.filter(available=True)

    @action(detail=True, methods=['get'])
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified studio.
        """
        try:
            studio = self.get_object()
            animes = Anime.objects.filter(studio_id=studio).order_by('id')
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'errors': _('Studio not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class GenreViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Genre instances.
    """
    serializer_class = GenreSerializer
    search_fields = ['name',]
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Genre.objects.filter(available=True)

    @action(detail=True, methods=['get'])
    def animes(self, request, pk=None):
        """
        Retrieve a list of animes for the specified genre.
        """
        try:
            genre = self.get_object()
            animes = Anime.objects.filter(genre_id=genre).order_by('id')
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response(
                {'errors': _('Genre not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class SeasonViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Season instances.
    """
    serializer_class = SeasonSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Season.objects.filter(available=True)


class DemographicViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Demographic instances.
    """
    serializer_class = DemographicSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Demographic.objects.filter(available=True)


class AuthorViewSet(LogicalDeleteMixin, viewsets.ModelViewSet):
    """
    Viewset for managing Author instances.
    """
    serializer_class = AuthorSerializer
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['id']

    def get_queryset(self):
        return Author.objects.filter(available=True)
