"""Views for Playlists App."""

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema_view

from apps.contents.models import Anime, Manga
from apps.utils.permissions import IsOwner
from .models import Playlist, PlaylistAnime, PlaylistManga
from .serializers import (
    PlaylistSerializer, PlaylistAnimeSerializer, PlaylistMangaSerializer)
from .schemas import (
    playlists_schemas, playlists_anime_schemas, playlists_manga_schemas)


@extend_schema_view(**playlists_schemas)
class PlaylistAPIView(APIView):
    """
    View for listing and creating playlists.

    Endpoints:
    - GET /api/v1/playlists/me/
    """
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)

    def get(self, request, format=None):
        """Get a list of playlists."""
        playlist = self.get_queryset()
        serializer = self.serializer_class(playlist, many=True)
        return Response(serializer.data)


@extend_schema_view(**playlists_anime_schemas)
class PlaylistAnimeAPIView(APIView):
    """
    View for listing and adding from a playlist.

    Endpoints:
    - GET /api/v1/playlists/animes/
    - POST /api/v1/playlists/animes/
    """
    permission_classes = [IsAuthenticated, IsOwner]
    cache_timeout = 7200  # Cache for 2 hours

    def get_queryset(self):
        playlist = Playlist.objects.get(user=self.request.user)
        return PlaylistAnime.objects.filter(playlist=playlist)

    def get(self, request):
        """Return the current user's playlist (anime)."""
        cache_key = f"playlist_anime_{request.user.id}"
        cached_data = cache.get(cache_key)

        if cached_data is None:
            queryset = self.get_queryset()
            if queryset.exists():
                serializer = PlaylistAnimeSerializer(queryset, many=True)
                cache.set(cache_key, serializer.data, self.cache_timeout)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"detail": "Empty anime playlist."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(cached_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Add an anime to the playlist."""
        playlist = Playlist.objects.get(user=self.request.user)

        # Params
        anime_id = request.data.get("anime_id")

        if not anime_id:
            return Response(
                {"detail": "'anime_id' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if PlaylistAnime.objects.filter(
                playlist=playlist, anime_id=anime_id).exists():
            return Response(
                {"detail": "Anime already in playlist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        anime = get_object_or_404(Anime, id=anime_id)
        playlist_anime = PlaylistAnime.objects.create(
            playlist=playlist,
            anime=anime,
        )

        # Invalidate cache
        cache_key = f"playlist_anime_{request.user.id}"
        cache.delete(cache_key)

        serializer = PlaylistAnimeSerializer(playlist_anime)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PlaylistAnimeDetailView(APIView):
    """
    View for update and remove from a playlist.

    Endpoints:
    - PATCH /api/v1/playlists/animes/{id}/
    - DELETE /api/v1/playlists/animes/{id}/
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def patch(self, request, item_id):
        """Update metadata status of a anime in the playlist."""
        playlist = get_object_or_404(Playlist, user=self.request.user)
        playlist_anime = get_object_or_404(
            PlaylistAnime,
            id=item_id,
            playlist=playlist,
        )

        status = request.data.get("status")
        is_watched = request.data.get("is_watched")
        is_favorite = request.data.get("is_favorite")

        if status is not None:
            playlist_anime.status = status

        if is_watched is not None:
            playlist_anime.is_watched = is_watched

        if is_favorite is not None:
            playlist_anime.is_favorite = is_favorite

        # Invalidate cache
        cache_key = f"playlist_anime_{request.user.id}"
        cache.delete(cache_key)

        playlist_anime.save()
        serializer = PlaylistAnimeSerializer(playlist_anime)
        return Response(serializer.data)

    def delete(self, request, item_id, format=None):
        """Remove an anime from the playlist."""
        playlist = get_object_or_404(Playlist, user=self.request.user)
        playlist_anime = get_object_or_404(
            PlaylistAnime,
            id=item_id,
            playlist=playlist,
        )

        # Invalidate cache
        cache_key = f"playlist_anime_{request.user.id}"
        cache.delete(cache_key)

        playlist_anime.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**playlists_manga_schemas)
class PlaylistMangaAPIView(APIView):
    """View for listing, adding, and removing mangas from a playlist.."""
    serializer_class = PlaylistMangaSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    CACHE_TIMEOUT = 7200  # Cache for 2 hours

    def get_queryset(self):
        playlist = Playlist.objects.get(user=self.request.user)
        return PlaylistManga.objects.filter(playlist=playlist)

    def get(self, request, pk=None):
        """Return the current user's playlist (manga)."""
        cache_key = f"playlist_manga_{request.user.id}"
        cached_data = cache.get(cache_key)

        if cached_data is None:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            cache.set(cache_key, serializer.data, self.CACHE_TIMEOUT)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(cached_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Add an manga to the playlist."""
        playlist = Playlist.objects.get(user=self.request.user)
        manga_id = request.data.get("manga_id")

        if not manga_id:
            return Response(
                {"errors": "manga_id is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if PlaylistManga.objects.filter(
                playlist=playlist, manga_id=manga_id).exists():
            return Response(
                {"errors": "Manga already in playlist"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        manga = get_object_or_404(Manga, id=manga_id)
        playlist_manga = PlaylistAnime.objects.create(
            playlist=playlist,
            manga=manga,
        )

        # Invalidate cache
        cache_key = f"playlist_manga_{request.user.id}"
        cache.delete(cache_key)

        serializer = self.serializer_class(playlist_manga)
        return Response(serializer.data)

    def patch(self, request, pk: None):
        """Update metadata status of a manga in the playlist."""
        playlist = get_object_or_404(Playlist, user=self.request.user)
        playlist_manga = get_object_or_404(
            PlaylistManga,
            id=pk,
            playlist=playlist,
        )

        status = request.data.get("status")
        is_watched = request.data.get("is_watched")
        is_favorite = request.data.get("is_favorite")

        if status is not None:
            playlist_manga.status = status

        if is_watched is not None:
            playlist_manga.is_watched = is_watched

        if is_favorite is not None:
            playlist_manga.is_favorite = is_favorite

        # Invalidate cache
        cache_key = f"playlist_manga_{request.user.id}"
        cache.delete(cache_key)

        playlist_manga.save()
        serializer = self.serializer_class(playlist_manga)
        return Response(serializer.data)

    def delete(self, request, pk=None, format=None):
        """Remove an manga from the playlist."""
        playlist = get_object_or_404(Playlist, user=self.request.user)
        playlist_manga = get_object_or_404(
            PlaylistManga,
            id=pk,
            playlist=playlist,
        )

        # Invalidate cache
        cache_key = f"playlist_manga_{request.user.id}"
        cache.delete(cache_key)

        playlist_manga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
