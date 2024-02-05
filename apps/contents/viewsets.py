"""Viewsets for Contents App."""

from django.http import Http404
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.utils.mixins import CreateMixin
from apps.contents.models import (Url, Studio, Genre, Season, Rating, Anime)
from apps.contents.serializers import (
    UrlSerializer, StudioSerializer, GenreSerializer, SeasonSerializer,
    RatingSerializer, AnimeSerializer
)


class UrlViewSet(viewsets.ModelViewSet, CreateMixin):
    """
    Viewset for managing Url instances.
    """
    serializer_class = UrlSerializer

    def get_queryset(self):
        return Url.objects.filter(available=True)

    def get_create_message(self):
        return _('Url created successfully.')


class StudioViewSet(viewsets.ModelViewSet, CreateMixin):
    """
    Viewset for managing Studio instances.
    """
    serializer_class = StudioSerializer
    filter_backends = [SearchFilter]
    search_fields = ['slug', 'name']

    def get_queryset(self):
        return Studio.objects.filter(available=True)

    def get_create_message(self):
        return _('Studio created successfully.')

    @action(detail=True, methods=['get'])
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified studio.
        """
        try:
            studio = self.get_object()
            animes = Anime.objects.filter(studio_id=studio)
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'errors': _('Studio not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class GenreViewSet(viewsets.ModelViewSet, CreateMixin):
    """
    Viewset for managing Genre instances.
    """
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.filter(available=True)

    def get_create_message(self):
        return _('Genre created successfully.')

    def destroy(self, request, *args, **kwargs):
        # Deletes the instance logically
        try:
            instance = self.get_object()
            instance.available = False
            instance.save()
            return Response(
                {'message': _('Genre deleted successfully.')}, status=status.HTTP_204_NO_CONTENT
            )
        except Http404:
            return Response(
                {'errors': _('Genre not found.')}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'errors': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=True, methods=['get'])
    def anime_list(self, request, pk=None):
        """
        Retrieve a list of animes for the specified genre.
        """
        try:
            genre = self.get_object()
            animes = Anime.objects.filter(genre_id=genre)
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'errors': _('Genre not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class SeasonViewSet(viewsets.ModelViewSet, CreateMixin):
    """
    Viewset for managing Season instances.
    """
    serializer_class = SeasonSerializer

    def get_queryset(self):
        return Season.objects.filter(available=True)

    def get_create_message(self):
        return _('Season created successfully.')


class RatingViewSet(viewsets.ModelViewSet, CreateMixin):
    """
    Viewset for managing Rating instances.
    """
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(available=True)

    def get_create_message(self):
        return _('Rating created successfully.')


class AnimeViewSet(viewsets.ModelViewSet, CreateMixin):
    """
    Viewset for managing Anime instances.
    """
    serializer_class = AnimeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name',]

    def get_queryset(self):
        return Anime.objects.filter(available=True)

    def get_create_message(self):
        return _('Anime created successfully.')
