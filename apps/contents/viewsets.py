"""Viewsets for Contents App."""

from django.http import Http404
from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
#from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.contents.models import (Url, Studio, Genre, Season, Rating, Anime)
from apps.contents.serializers import (
    UrlSerializer, StudioSerializer, GenreSerializer, SeasonSerializer,
    RatingSerializer, AnimeSerializer
)


class UrlViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Url instances.
    """
    serializer_class = UrlSerializer
    search_fields = ['url', 'tag']
    ordering_fields = ['tag']

    def get_queryset(self):
        return Url.objects.filter(available=True).order_by('id')


class StudioViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Studio instances.
    """
    serializer_class = StudioSerializer
    search_fields = ['name']
    ordering_fields = ['name']

    def get_queryset(self):
        return Studio.objects.filter(available=True).order_by('id')

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


class GenreViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Genre instances.
    """
    serializer_class = GenreSerializer
    search_fields = ['name',]
    ordering_fields = ['name']

    def get_queryset(self):
        return Genre.objects.filter(available=True).order_by('id')

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
            animes = Anime.objects.filter(genre_id=genre).order_by('id')
            serializer = AnimeSerializer(animes, many=True)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'errors': _('Genre not found.')}, status=status.HTTP_404_NOT_FOUND
            )


class SeasonViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Season instances.
    """
    serializer_class = SeasonSerializer
    search_fields = ['name']
    ordering_fields = ['name']

    def get_queryset(self):
        return Season.objects.filter(available=True).order_by('id')


class RatingViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Rating instances.
    """
    serializer_class = RatingSerializer
    search_fields = ['name']
    ordering_fields = ['name']

    def get_queryset(self):
        return Rating.objects.filter(available=True).order_by('id')


class AnimeViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Anime instances.
    """
    serializer_class = AnimeSerializer
    search_fields = ['name', 'studio_id__name']
    ordering_fields = ['name']

    def get_queryset(self):
        return Anime.objects.filter(available=True).order_by('id')
