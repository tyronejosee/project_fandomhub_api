"""Viewsets for Playlists App."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.playlists.models import Playlist, PlaylistItem
from apps.playlists.serializers import (
    PlaylistSerializer, PlaylistItemSerializer
)


class PlaylistViewSet(viewsets.ModelViewSet):
    serializer_class = PlaylistSerializer
    ordering = ["id"]

    def get_queryset(self):
        user = self.request.user
        return Playlist.objects.filter(user=user)

    @action(detail=True, methods=["get"], url_path="animes")
    def anime_list(self, request, pk=None):
        """Pending."""
        playlist = self.get_object()
        playlists = PlaylistItem.objects.filter(
            playlist=playlist,
            anime__isnull=False
        )
        serializer = PlaylistItemSerializer(playlists, many=True)
        print(serializer.data)
        return Response(serializer.data)
