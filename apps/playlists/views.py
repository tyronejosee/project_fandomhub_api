"""Viewsets for Playlists App."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Playlist, PlaylistAnime
from .serializers import PlaylistSerializer, PlaylistAnimeSerializer


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
        playlists = PlaylistAnime.objects.filter(playlist=playlist)
        serializer = PlaylistAnimeSerializer(playlists, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['post'])
    # def add_anime(self, request, pk=None):
    #     """Pending."""
    #     playlist = self.get_object()
    #     anime_id = request.data.get('anime_id')
    #     rating = request.data.get('rating')

    #     if not anime_id or not rating:
    #         return Response(
    #             {'error': 'anime_id and rating are required'},
    #             status=status.HTTP_400_BAD_REQUEST
    #         )

    #     try:
    #         anime = Anime.objects.get(pk=anime_id)
    #     except Anime.DoesNotExist:
    #         return Response({'error': 'Anime not found'}, status=404)

    #     playlist_anime, created = PlaylistAnime.objects.get_or_create(
    #         playlist=playlist, anime=anime
    #     )
    #     playlist_anime.rating = rating
    #     playlist_anime.save()

    #     serializer = PlaylistSerializer(playlist)
    #     return Response(serializer.data)
