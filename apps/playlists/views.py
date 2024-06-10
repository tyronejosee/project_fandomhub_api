"""Views for Playlists App."""

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsMember
from .models import AnimeList, AnimeListItem
from .serializers import (
    AnimeListReadSerializer,
    AnimeListWriteSerializer,
    AnimeListItemReadSerializer,
    AnimeListItemWriteSerializer,
)


class MyAnimeListView(APIView):
    """
    View for listing and adding from a playlist.

    Endpoints:
    - GET /api/v1/playlists/myanimelist/
    - PATCH /api/v1/playlists/myanimelist/
    """

    permission_classes = [IsMember]

    def get_queryset(self):
        return AnimeList.objects.get(user=self.request.user)

    def get(self, request):
        # Get the profile of the animelist
        animelist = self.get_queryset()
        if animelist:
            serializer = AnimeListReadSerializer(animelist)
            return Response(serializer.data)
        return Response({"detail": "No Animelist."}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        # Update the profile of the animelist
        animelist = self.get_queryset()
        if animelist:
            serializer = AnimeListWriteSerializer(
                animelist, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "No Animelist."}, status=status.HTTP_404_NOT_FOUND)


class MyAnimeListItemsView(APIView):
    """
    Pending.

    Endpoints:
    - GET /api/v1/playlists/myanimelist/animes/
    - POST /api/v1/playlists/myanimelist/animes/
    """

    def get_queryset(self):
        return AnimeList.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        # Retrieve all animes from the animelist
        animelist = self.get_queryset()
        items = AnimeListItem.objects.filter(animelist_id=animelist, is_available=True)

        if items.exists():
            serializer = AnimeListItemReadSerializer(items, many=True)
            return Response(serializer.data)
        return Response({"detail": "Your animelist is empty."})

    def post(self, request, *args, **kwargs):
        # Add an anime to the animelist
        animelist = self.get_queryset()
        anime_id = request.data.get("anime_id")

        if AnimeListItem.objects.filter(
            animelist_id=animelist, anime_id=anime_id
        ).exists():
            return Response(
                {"detail": "Anime already in animelist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = AnimeListItemWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(animelist_id=animelist)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyAnimeListItemsDetailView(APIView):
    """
    Pending.

    Endpoints:
    - GET /api/v1/playlists/myanimelist/animes/{id}/
    - PATCH /api/v1/playlists/myanimelist/animes/{id}/
    - DELETE /api/v1/playlists/myanimelist/animes/{id}/
    """

    def get_object(self, item_id):
        return get_object_or_404(AnimeListItem, pk=item_id)

    def get(self, request, item_id):
        # Retrieve an anime from the animelist
        anime = self.get_object(item_id)
        serializer = AnimeListItemReadSerializer(anime)
        return Response(serializer.data)

    def patch(self, request, item_id):
        # Update an anime in the animelist
        anime = self.get_object(item_id)
        serializer = AnimeListItemWriteSerializer(
            anime, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        # Remove an anime from the animelist
        item = self.get_object(item_id)
        item.is_available = False  # Logical deletion
        item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
