@method*decorator(cache_page(60 * 60 \_ 2))
@method_decorator(vary_on_cookie)
def list(self, request, *args, \*\*kwargs):
return super().list(request, *args, \*\*kwargs)

@method*decorator(cache_page(60 * 60 \_ 2))
@method_decorator(vary_on_cookie)
def retrieve(self, request, *args, \*\*kwargs):
return super().retrieve(request, *args, \*\*kwargs)

def create(self, request, *args, \*\*kwargs):
response = super().create(request, *args, \*\*kwargs)
cache.clear()
return response

---

# @action(detail=True, methods=['post'])

# def add_anime(self, request, pk=None):

# """Pending."""

# playlist = self.get_object()

# anime_id = request.data.get('anime_id')

# rating = request.data.get('rating')

# if not anime_id or not rating:

# return Response(

# {'error': 'anime_id and rating are required'},

# status=status.HTTP_400_BAD_REQUEST

# )

# try:

# anime = Anime.objects.get(pk=anime_id)

# except Anime.DoesNotExist:

# return Response({'error': 'Anime not found'}, status=404)

# playlist_anime, created = PlaylistAnime.objects.get_or_create(

# playlist=playlist, anime=anime

# )

# playlist_anime.rating = rating

# playlist_anime.save()

# serializer = PlaylistSerializer(playlist)

# return Response(serializer.data)

---

rating = models.PositiveSmallIntegerField(
default=0, validators=[MinValueValidator(1), MaxValueValidator(10)])
status = models.CharField(
max_length=20, choices=STATUS_CHOICES,
default="pending", db_index=True
)
is_watched = models.BooleanField(default=False, db_index=True)
tags = models.CharField(max_length=255, blank=True)
comments = models.TextField(blank=True)

---

"""Viewsets for Playlists App."""

from django.utils.translation import gettext as \_
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from apps.utils.permissions import IsOwner
from apps.playlists.models import Playlist, PlaylistAnime, PlaylistManga
from apps.playlists.serializers import (
PlaylistSerializer, PlaylistAnimeSerializer, PlaylistMangaSerializer
)

class PlaylistViewSet(ModelViewSet):
"""ViewSet for managing playlists."""

    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    ordering = ["id"]

    def get_queryset(self):
        # Return the playlists for the current user
        user = self.request.user
        return Playlist.objects.filter(user=user)

    def perform_create(self, serializer):
        # Save the playlist with the current user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"], url_path="animes")
    def get_anime_list(self, request, pk=None):
        """Get the list of anime in the playlist."""
        playlist = self.get_object()
        playlists = PlaylistAnime.objects.filter(
            playlist=playlist,
        )
        if playlists:
            serializer = PlaylistAnimeSerializer(playlists, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No content available."},
            status=status.HTTP_404_NOT_FOUND
        )

    @action(detail=True, methods=["get"], url_path="mangas")
    def get_manga_list(self, request, pk=None):
        """Get the list of anime in the playlist."""
        playlist = self.get_object()
        playlists = PlaylistManga.objects.filter(
            playlist=playlist,
        )
        if playlists:
            serializer = PlaylistMangaSerializer(playlists, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No content available."},
            status=status.HTTP_404_NOT_FOUND
        )

class PlaylistAnimeViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
"""ViewSet for managing anime in playlists."""

    serializer_class = PlaylistAnimeSerializer
    ordering = ["id"]    # Add order field

    def get_queryset(self):
        # Return the manga in the current playlist
        user = self.request.user
        playlist = Playlist.objects.get(user=user)
        return PlaylistAnime.objects.filter(playlist=playlist)

    @action(detail=True, methods=["post"], url_path="mark-favorite")
    def switch_is_favorite(self, request, pk=None):
        """Mark an anime as favorite or not."""
        playlist_item = self.get_object()
        playlist_item.is_favorite = not playlist_item.is_favorite
        playlist_item.save()

        message = (
            _("Anime marked as favorite.")
            if playlist_item.is_favorite
            else _("Anime not marked as favorite.")
        )

        return Response(
            {"message": message},
            status=status.HTTP_200_OK
        )

class PlaylistMangaViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
"""ViewSet for managing manga in playlists."""

    serializer_class = PlaylistMangaSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    ordering = ["id"]    # Add order field

    def get_queryset(self):
        # Return the manga in the current playlist
        user = self.request.user
        playlist = Playlist.objects.get(user=user)
        return PlaylistManga.objects.filter(playlist=playlist)
