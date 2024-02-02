"""Viewsets for Contents App."""

from rest_framework import viewsets
from apps.contents.models import (
    Url, Studio, Genre, Premiered, Rating, Content
)
from apps.contents.serializers import (
    UrlSerializer, StudioSerializer, GenreSerializer, PremieredSerializer,
    RatingSerializer, ContentSerializer
)


class UrlViewSet(viewsets.ModelViewSet):
    """Viewset for managing Url instances."""
    serializer_class = UrlSerializer

    def get_queryset(self):
        return Url.objects.all()


class StudioViewSet(viewsets.ModelViewSet):
    """Viewset for managing Studio instances."""
    serializer_class = StudioSerializer

    def get_queryset(self):
        return Studio.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
    """Viewset for managing Genre instances."""
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()


class PremieredViewSet(viewsets.ModelViewSet):
    """Viewset for managing Premiered instances."""
    serializer_class = PremieredSerializer

    def get_queryset(self):
        return Premiered.objects.all()


class RatingViewSet(viewsets.ModelViewSet):
    """Viewset for managing Rating instances."""
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.all()


class ContentViewSet(viewsets.ModelViewSet):
    """Viewset for managing Content instances."""
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.all()
