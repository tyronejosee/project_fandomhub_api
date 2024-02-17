"""Viewsets for Contents App."""

# from django.utils.translation import gettext as _
from rest_framework import viewsets
# from rest_framework.decorators import action
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

    # @action(detail=False, methods=['get'], url_path='populars')
    # def popular_list(self, request, pk=None):
    #     """
    #     Retrieve a list of animes for the specified genre.
    #     """
    #     genre = self.get_object()
    #     anime_list = Anime.objects.filter(genre_id=genre)
    #     if anime_list.exists():
    #         serializer = AnimeSerializer(anime_list, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(
    #         {'detail': _('There are no animes for this genre.')},
    #         status=status.HTTP_404_NOT_FOUND
    #     )


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
