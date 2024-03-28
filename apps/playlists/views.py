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


class PlaylistAPIView(APIView):
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


class PlaylistAnimeAPIView(APIView):
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

        if not anime_id:
            return Response(
                {"errors": "anime_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if PlaylistAnime.objects.filter(
                playlist=playlist, anime_id=anime_id).exists():
            return Response(
                {"errors": "Anime already in playlist"},
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
        playlist = get_object_or_404(Playlist, user=self.request.user)
        playlist_anime = get_object_or_404(
            PlaylistAnime,
            id=pk,
            playlist=playlist,
        )
        playlist_anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk: None):
        playlist = get_object_or_404(Playlist, user=self.request.user)
        playlist_anime = get_object_or_404(
            PlaylistAnime,
            id=pk,
            playlist=playlist,
        )

        is_watched = request.data.get("is_watched")
        is_favorite = request.data.get("is_favorite")

        if is_watched is not None:
            playlist_anime.is_watched = is_watched

        if is_favorite is not None:
            playlist_anime.is_favorite = is_favorite

        playlist_anime.save()
        serializer = self.serializer_class(playlist_anime)
        return Response(serializer.data)
