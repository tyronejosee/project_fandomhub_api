"""Viewsets for Playlists App."""

from django.utils.translation import gettext as _
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.playlists.models import Playlist, PlaylistAnime, PlaylistManga
from apps.playlists.serializers import (
    PlaylistSerializer, PlaylistAnimeSerializer, PlaylistMangaSerializer
)


class PlaylistViewSet(viewsets.ModelViewSet):
    """ViewSet for managing playlists."""

    serializer_class = PlaylistSerializer
    ordering = ["id"]

    def get_queryset(self):
        # Return the playlists for the current user
        user = self.request.user
        return Playlist.objects.filter(user=user)

    def perform_create(self, serializer):
        # Save the playlist with the current user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["get"], url_path="animes")
    def anime_list(self, request, pk=None):
        """Get the list of anime in the playlist."""
        playlist = self.get_object()
        playlists = PlaylistAnime.objects.filter(
            playlist=playlist,
        )
        serializer = PlaylistAnimeSerializer(playlists, many=True)
        return Response(serializer.data)


class PlaylistAnimeViewSet(viewsets.ModelViewSet):
    """ViewSet for managing anime in playlists."""

    serializer_class = PlaylistAnimeSerializer
    ordering = ["id"]    # Add order field

    def get_queryset(self):
        # Return the anime in the current playlist
        if hasattr(self, "playlist"):
            return PlaylistAnime.objects.filter(playlist=self.playlist)
        user = self.request.user
        self.playlist = Playlist.objects.get(user=user)
        return (
            PlaylistAnime.objects
            .filter(playlist=self.playlist)
            .select_related("playlist")
        )

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


class PlaylistMangaViewSet(viewsets.ModelViewSet):
    """ViewSet for managing manga in playlists."""

    serializer_class = PlaylistMangaSerializer
    ordering = ["id"]    # Add order field

    def get_queryset(self):
        # Return the manga in the current playlist
        if hasattr(self, "playlist"):
            return PlaylistManga.objects.filter(playlist=self.playlist)
        user = self.request.user
        self.playlist = Playlist.objects.get(user=user)
        return (
            PlaylistManga.objects
            .filter(playlist=self.playlist)
            .select_related("playlist")
        )
