"""Views for Playlists App."""

from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

from apps.animes.models import Anime
from apps.mangas.models import Manga
from apps.utils.permissions import IsOwner
from .models import Playlist, PlaylistItem
from .serializers import (
    PlaylistReadSerializer,
    PlaylistWriteSerializer,
    PlaylistItemReadSerializer,
    PlaylistItemWriteSerializer,
)
from .choices import StatusChoices


class PlaylistViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    search_fields = ["name"]
    ordering_fields = ["name"]
    ordering = ["-created_at"]

    ALLOWED_MODELS = [Anime, Manga]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Playlist.objects.all()
        return Playlist.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return PlaylistWriteSerializer
        return PlaylistReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied(
                _("You do not have permission to edit this playlist.")
            )
        serializer.save()

    @action(detail=True, methods=["get"])
    def items(self, request, pk=None):
        """Pending."""
        playlist = self.get_object()
        items = playlist.playlistitem_set.all()
        serializer = PlaylistItemReadSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def add_item(self, request, pk=None):
        """Pending."""
        playlist = self.get_object()
        data = request.data
        uuid = data.get("uuid")

        try:
            content_type = ContentType.objects.get_for_model(
                PlaylistItem.content_object.related_model
            )
            model_class = content_type.model_class()
            object_id = get_object_or_404(model_class, pk=uuid).pk
        except (ContentType.DoesNotExist, ValueError, model_class.DoesNotExist):
            raise Http404(_("Invalid UUID"))

        if model_class not in self.ALLOWED_MODELS:
            raise Http404(_("Model not allowed"))

        playlist_item_data = {
            "playlist": playlist.pk,
            "content_type": content_type.pk,
            "object_id": object_id,
            "status": data.get("status", StatusChoices.PENDING),
            "is_watched": data.get("is_watched", False),
            "is_favorite": data.get("is_favorite", False),
            "order": data.get("order", 0),
        }
        serializer = PlaylistItemWriteSerializer(data=playlist_item_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PlaylistAnimeListView(APIView):
#     """
#     View for listing and adding from a playlist.

#     Endpoints:
#     - GET /api/v1/playlists/animes/
#     - POST /api/v1/playlists/animes/
#     """

#     permission_classes = [IsAuthenticated, IsOwner]
#     cache_timeout = 7200  # Cache for 2 hours

#     def get_queryset(self):
#         playlist = Playlist.objects.get(user=self.request.user)
#         return PlaylistAnime.objects.filter(playlist=playlist)

#     def get(self, request):
#         """Return the current user's playlist (anime)."""
#         cache_key = f"playlist_anime_{request.user.id}"
#         cached_data = cache.get(cache_key)

#         if cached_data is None:
#             queryset = self.get_queryset()
#             if queryset.exists():
#                 serializer = PlaylistAnimeSerializer(queryset, many=True)
#                 cache.set(cache_key, serializer.data, self.cache_timeout)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(
#                 {"detail": "Empty anime playlist."}, status=status.HTTP_404_NOT_FOUND
#             )

#         return Response(cached_data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         """Add an anime to the playlist."""
#         playlist = Playlist.objects.get(user=self.request.user)

#         # Params
#         anime_id = request.data.get("anime_id")

#         if not anime_id:
#             return Response(
#                 {"detail": "'anime_id' is required."},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         if PlaylistAnime.objects.filter(playlist=playlist, anime_id=anime_id).exists():
#             return Response(
#                 {"detail": "Anime already in playlist."},
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         anime = get_object_or_404(Anime, id=anime_id)
#         playlist_anime = PlaylistAnime.objects.create(
#             playlist=playlist,
#             anime=anime,
#         )

#         # Invalidate cache
#         cache_key = f"playlist_anime_{request.user.id}"
#         cache.delete(cache_key)

#         serializer = PlaylistAnimeSerializer(playlist_anime)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class PlaylistAnimeDetailView(APIView):
#     """
#     View for update and remove from a playlist.

#     Endpoints:
#     - PATCH /api/v1/playlists/animes/{id}/
#     - DELETE /api/v1/playlists/animes/{id}/
#     """

#     permission_classes = [IsAuthenticated, IsOwner]

#     def patch(self, request, item_id):
#         """Update metadata status of a anime in the playlist."""
#         playlist = get_object_or_404(Playlist, user=self.request.user)
#         playlist_anime = get_object_or_404(
#             PlaylistAnime,
#             id=item_id,
#             playlist=playlist,
#         )

#         status = request.data.get("status")
#         is_watched = request.data.get("is_watched")
#         is_favorite = request.data.get("is_favorite")

#         if status is not None:
#             playlist_anime.status = status

#         if is_watched is not None:
#             playlist_anime.is_watched = is_watched

#         if is_favorite is not None:
#             playlist_anime.is_favorite = is_favorite

#         # Invalidate cache
#         cache_key = f"playlist_anime_{request.user.id}"
#         cache.delete(cache_key)

#         playlist_anime.save()
#         serializer = PlaylistAnimeSerializer(playlist_anime)
#         return Response(serializer.data)

#     def delete(self, request, item_id, format=None):
#         """Remove an anime from the playlist."""
#         playlist = get_object_or_404(Playlist, user=self.request.user)
#         playlist_anime = get_object_or_404(
#             PlaylistAnime,
#             id=item_id,
#             playlist=playlist,
#         )

#         # Invalidate cache
#         cache_key = f"playlist_anime_{request.user.id}"
#         cache.delete(cache_key)

#         playlist_anime.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
