"""Views for Playlists App."""

import tempfile
import zipfile
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.animes.models import Anime
from apps.mangas.models import Manga
from apps.users.permissions import IsMember
from .models import AnimeList, AnimeListItem, MangaList, MangaListItem
from .serializers import (
    AnimeListReadSerializer,
    AnimeListWriteSerializer,
    AnimeListItemReadSerializer,
    AnimeListItemWriteSerializer,
    MangaListReadSerializer,
    MangaListWriteSerializer,
    MangaListItemReadSerializer,
    MangaListItemWriteSerializer,
)


class AnimeListView(APIView):
    """
    View to fetch and update the AnimeList profile.

    Endpoints:
    - GET /api/v1/playlists/animelist/
    - PATCH /api/v1/playlists/animelist/
    """

    permission_classes = [IsMember]

    def get_queryset(self):
        try:
            return AnimeList.objects.get(user=self.request.user)
        except AnimeList.DoesNotExist:
            return AnimeList.objects.create(user=self.request.user)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Get the profile of the animelist
        animelist = self.get_queryset()
        serializer = AnimeListReadSerializer(animelist)
        return Response(serializer.data)

    def patch(self, request):
        # Update the profile of the animelist
        animelist = self.get_queryset()

        try:
            serializer = AnimeListWriteSerializer(
                animelist, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AnimeListItemView(APIView):
    """
    View to add an anime to AnimeList.

    Endpoints:
    - GET /api/v1/playlists/animelist/animes/
    - POST /api/v1/playlists/animelist/animes/
    """

    permission_classes = [IsMember]

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

        try:
            anime = get_object_or_404(Anime, id=anime_id)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = AnimeListItem.objects.filter(
                animelist_id=animelist, anime_id=anime
            ).first()
            if item:
                if item.is_available:
                    return Response(
                        {"detail": "Anime already in animelist."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                else:
                    item.is_available = True
                    item.save()
                    serializer = AnimeListItemWriteSerializer(item)
                    return Response(serializer.data, status=status.HTTP_200_OK)

            serializer = AnimeListItemWriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(animelist_id=animelist)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AnimeListItemDetailView(APIView):
    """
    View to retrieve, update, and delete an anime from AnimeList.

    Endpoints:
    - GET /api/v1/playlists/animelist/animes/{id}/
    - PATCH /api/v1/playlists/animelist/animes/{id}/
    - DELETE /api/v1/playlists/animelist/animes/{id}/
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


# MangaList


class MangaListView(APIView):
    """
    View to fetch and update the MangaList profile.

    Endpoints:
    - GET /api/v1/playlists/mangalist/
    - PATCH /api/v1/playlists/mangalist/
    """

    permission_classes = [IsMember]

    def get_queryset(self):
        try:
            return MangaList.objects.get(user=self.request.user)
        except MangaList.DoesNotExist:
            return MangaList.objects.create(user=self.request.user)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Get the profile of the mangalist
        mangalist = self.get_queryset()
        serializer = MangaListReadSerializer(mangalist)
        return Response(serializer.data)

    def patch(self, request):
        # Update the profile of the mangalist
        mangalist = self.get_queryset()

        try:
            serializer = MangaListWriteSerializer(
                mangalist, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MangaListItemView(APIView):
    """
    View to add an manga to MangaList.

    Endpoints:
    - GET /api/v1/playlists/mangalist/mangas/
    - POST /api/v1/playlists/mangalist/mangas/
    """

    permission_classes = [IsMember]

    def get_queryset(self):
        return MangaList.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        # Retrieve all mangas from the mangalist
        mangalist = self.get_queryset()

        items = MangaListItem.objects.filter(mangalist_id=mangalist, is_available=True)

        if items.exists():
            serializer = MangaListItemReadSerializer(items, many=True)
            return Response(serializer.data)
        return Response({"detail": "Your mangalist is empty."})

    def post(self, request, *args, **kwargs):
        # Add an manga to the mangalist
        mangalist = self.get_queryset()
        manga_id = request.data.get("manga_id")

        try:
            manga = get_object_or_404(Manga, id=manga_id)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item = MangaListItem.objects.filter(
                mangalist_id=mangalist, manga_id=manga
            ).first()
            if item:
                if item.is_available:
                    return Response(
                        {"detail": "Manga already in mangalist."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                else:
                    item.is_available = True
                    item.save()
                    serializer = MangaListItemWriteSerializer(item)
                    return Response(serializer.data, status=status.HTTP_200_OK)

            serializer = MangaListItemWriteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(mangalist_id=mangalist)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MangaListItemDetailView(APIView):
    """
    View to retrieve, update, and delete an manga from MangaList.

    Endpoints:
    - GET /api/v1/playlists/mangalist/mangas/{id}/
    - PATCH /api/v1/playlists/mangalist/mangas/{id}/
    - DELETE /api/v1/playlists/mangalist/mangas/{id}/
    """

    def get_object(self, item_id):
        return get_object_or_404(MangaListItem, pk=item_id)

    def get(self, request, item_id):
        # Retrieve an manga from the mangalist
        manga = self.get_object(item_id)
        serializer = MangaListItemReadSerializer(manga)
        return Response(serializer.data)

    def patch(self, request, item_id):
        # Update an manga in the mangalist
        manga = self.get_object(item_id)
        serializer = MangaListItemWriteSerializer(
            manga, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id):
        # Remove an manga from the mangalist
        item = self.get_object(item_id)
        item.is_available = False  # Logical deletion
        item.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MangaListExportView(APIView):
    """
    View to export data as a ZIP file for the items within the MangaList.

    Endpoint:
    - GET /api/v1/playlists/mangalist/export/
    """

    permission_classes = [IsMember]

    def get(self, request, *args, **kwargs):
        # Retrieve all items from the mangalist
        mangalist = MangaList.objects.get(user=self.request.user)
        items = MangaListItem.objects.filter(mangalist_id=mangalist, is_available=True)

        # TODO: Testing and validating the endpoint
        if items.exists():
            # Create a temporary file to write the JSON data
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            with zipfile.ZipFile(temp_file, "w") as zip_file:
                for item in items:
                    data = MangaListItemReadSerializer(item).data
                    zip_file.writestr(f"{item.id}.json", str(data))

            # Read the temporary file and prepare the response
            with open(temp_file.name, "rb") as file:
                response = HttpResponse(file.read(), content_type="application/zip")
                response["Content-Disposition"] = (
                    'attachment; filename="mangalist_export.zip"'
                )
            return response
        return Response({"detail": "Your mangalist is empty."})
