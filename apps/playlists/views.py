"""Views for Playlists App."""

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contents.models import Anime
from apps.utils.permissions import IsOwner

from .models import Playlist
from .models import PlaylistAnime
from .serializers import PlaylistAnimeSerializer
from .serializers import PlaylistSerializer


class PlaylistList(APIView):
    """View for listing and creating playlists."""
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def get(self, request, format=None):
        """Get a list of playlists."""
        playlist = self.get_queryset()
        serializer = self.serializer_class(playlist, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new playlist."""
        serializer = self.self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid(user=request.user):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistAnimeList(APIView):
    """View for listing, adding, and removing anime from a playlist.."""
    serializer_class = PlaylistAnimeSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        playlist = Playlist.objects.get(user=self.request.user)
        return PlaylistAnime.objects.filter(playlist=playlist)

    def get(self, request, pk=None):
        """Return the current user's playlist."""
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Add an anime to the playlist."""
        playlist = Playlist.objects.get(user=self.request.user)
        anime_id = request.data.get("anime_id")

        if PlaylistAnime.objects.filter(
                playlist=playlist, anime_id=anime_id).exists():
            return Response(
                {"error": "Anime already in playlist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not anime_id:
            return Response(
                {"error": "anime_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        anime = get_object_or_404(Anime, id=anime_id)
        playlist_anime = PlaylistAnime.objects.create(
            playlist=playlist,
            anime=anime,
        )
        serializer = self.serializer_class(playlist_anime)
        return Response(serializer.data)

    def delete(self, request, pk=None, format=None):
        """Remove an anime from the playlist."""
        playlist = Playlist.objects.get(user=self.request.user)
        playlist_anime = get_object_or_404(
            PlaylistAnime,
            id=pk,
            playlist=playlist,
        )
        playlist_anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
