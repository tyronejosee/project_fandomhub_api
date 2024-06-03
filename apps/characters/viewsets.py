"""ViewSets for Characters App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.utils.mixins import LogicalDeleteMixin
from apps.utils.models import Picture
from apps.utils.serializers import PictureReadSerializer, PictureWriteSerializer
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.models import CharacterVoice
from apps.persons.models import Person
from apps.persons.serializers import PersonMinimalSerializer
from apps.users.permissions import IsContributor
from apps.users.choices import RoleChoices
from .models import Character, CharacterAnime, CharacterManga
from .serializers import CharacterReadSerializer, CharacterWriteSerializer


class CharacterViewSet(LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Characters instances.

    Endpoints:
    - GET /api/v1/characters/
    - POST /api/v1/characters/
    - GET /api/v1/characters/{id}/
    - PUT /api/v1/characters/{id}/
    - PATCH /api/v1/characters/{id}/
    - DELETE /api/v1/characters/{id}/
    """

    serializer_class = CharacterWriteSerializer
    search_fields = ["name", "name_kanji"]
    ordering_fields = ["name", "role"]

    def get_queryset(self):
        return Character.objects.get_available()

    def get_permissions(self):
        if self.action in [
            "list",
            "retrieve",
            "picture_list",
            "voices_list",
            "anime_for_character",
            "manga_for_character",
        ]:
            return [AllowAny()]
        return [IsContributor()]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CharacterReadSerializer
        return super().get_serializer_class()

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    @action(detail=True, methods=["get", "post"], url_path="pictures")
    def picture_list(self, request, pk=None, *args, **kwargs):
        """
        Action lists and creates pictures for a character.

        Endpoints:
        - GET api/v1/characters/{id}/pictures/
        - POST api/v1/characters/{id}/pictures/
        """
        if request.method == "GET":
            # Get all the pictures of a character
            character = self.get_object()
            pictures = Picture.objects.filter(
                content_type=ContentType.objects.get_for_model(Character),
                object_id=character.id,
            )

            # TODO: Add pagination
            if pictures:
                serializer = PictureReadSerializer(pictures, many=True)
                return Response(serializer.data)

            return Response(
                {"detail": "There is no pictures associated with this character."},
                status=status.HTTP_404_NOT_FOUND,
            )

        elif request.method == "POST":
            # Create a picture for the character
            if not request.user.role == RoleChoices.CONTRIBUTOR:
                return Response(
                    {"detail": _("You do not have permission to create pictures.")},
                    status=status.HTTP_403_FORBIDDEN,
                )

            serializer = PictureWriteSerializer(data=request.data)

            if serializer.is_valid():
                character = self.get_object()
                character_model = ContentType.objects.get_for_model(Character)
                serializer.save(
                    content_type=character_model,
                    object_id=character.pk,
                )
                return Response(
                    {"detail": "Picture uploaded successfully."},
                    status=status.HTTP_201_CREATED,
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    @action(detail=True, methods=["get"], url_path="voices")
    def voices_list(self, request, pk=None):
        try:
            character = self.get_object()
            character_anime = CharacterVoice.objects.filter(character_id=character)
            voice_ids = character_anime.values_list("voice_id", flat=True)
            persons = Person.objects.filter(id__in=voice_ids)
            serializer = PersonMinimalSerializer(persons, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Character.DoesNotExist:
            return Response(
                {"detail": "Character not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    @action(detail=True, methods=["get"], url_path="anime")
    def anime_for_character(self, request, pk=None, *args, **kwargs):
        """
        Action retrieve the anime associated with a character.

        Endpoints:
        - GET api/v1/characters/{id}/anime/
        """
        try:
            character = self.get_object()
            character_anime = CharacterAnime.objects.filter(
                character_id=character
            ).first()

            if character_anime:
                anime = character_anime.anime_id
                serializer = AnimeMinimalSerializer(anime)
                return Response(serializer.data)

            return Response(
                {"detail": "There is no anime associated with this character."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Character.DoesNotExist:
            return Response(
                {"detail": "Character not found."}, status=status.HTTP_404_NOT_FOUND
            )

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    @action(detail=True, methods=["get"], url_path="manga")
    def manga_for_character(self, request, pk=None, *args, **kwargs):
        """
        Action retrieve the manga associated with a character.

        Endpoints:
        - GET api/v1/characters/{id}/manga/
        """
        try:
            character = self.get_object()
            character_manga = CharacterManga.objects.filter(
                character_id=character
            ).first()

            if character_manga:
                manga = character_manga.manga_id
                serializer = MangaMinimalSerializer(manga)
                return Response(serializer.data)

            return Response(
                {"detail": "There is no manga associated with this character."},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Character.DoesNotExist:
            return Response(
                {"detail": "Character not found."}, status=status.HTTP_404_NOT_FOUND
            )
