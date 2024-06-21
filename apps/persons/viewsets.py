"""ViewSets for Persons App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext as _
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utils.models import Picture
from apps.utils.pagination import MediumSetPagination
from apps.utils.serializers import PictureReadSerializer, PictureWriteSerializer
from apps.users.permissions import IsContributor
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.models import CharacterVoice
from apps.characters.serializers import CharacterVoiceReadSerializer
from .models import Person
from .serializers import (
    PersonReadSerializer,
    PersonWriteSerializer,
    PersonMinimalSerializer,
)
from .choices import CategoryChoices
from .filters import PersonFilter
from .schemas import person_schemas


@extend_schema_view(**person_schemas)
class PersonViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Person instances.

    Endpoints:
    - GET /api/v1/persons/
    - POST /api/v1/persons/
    - GET /api/v1/persons/{id}/
    - PUT /api/v1/persons/{id}/
    - PATCH /api/v1/persons/{id}/
    - DELETE /api/v1/persons/{id}/
    """

    permission_classes = [IsContributor]
    serializer_class = PersonWriteSerializer
    search_fields = ["name", "given_name", "family_name"]
    filterset_class = PersonFilter

    def get_queryset(self):
        return Person.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return PersonMinimalSerializer
        elif self.action == "retrieve":
            return PersonReadSerializer
        return super().get_serializer_class()

    @extend_schema(
        summary="Get Mangas for Author",
        description="Retrieve a list of mangas for author.",
    )
    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="mangas",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    def get_mangas(self, request, pk=None, *args, **kwargs):
        """
        Action retrieve mangas associated with a author.

        Endpoints:
        - GET api/v1/persons/{id}/mangas/
        """
        person = self.get_object()
        category = person.category
        if category != CategoryChoices.WRITER:
            return Response(
                {
                    "detail": _(
                        f"This person is not a writer, current {category.upper()}."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        manga_list = person.manga_set.all()
        # manga_list = Manga.objects.filter(author_id=pk)
        if manga_list.exists():
            paginator = MediumSetPagination()
            paginated_data = paginator.paginate_queryset(manga_list, request)
            serializer = MangaMinimalSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": _("There are no mangas for this author.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent", "Accept-Language"))
    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="pictures",
    )
    def get_pictures(self, request, *args, **kwargs):
        """
        Action retrieve pictures associated with a person.

        Endpoints:
        - GET api/v1/persons/{id}/pictures/
        """
        person = self.get_object()
        pictures = Picture.objects.filter(
            content_type=ContentType.objects.get_for_model(Person),
            object_id=person.id,
        )  # TODO: Add manager
        if pictures:
            serializer = PictureReadSerializer(pictures, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": _("No pictures found for this person.")},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsContributor],
        url_path="create-picture",
    )
    def create_picture(self, request, pk=None, *args, **kwargs):
        """
        Action create a picture for the person.

        Endpoints:
        - POST api/v1/persons/{id}/pictures/
        """
        serializer = PictureWriteSerializer(data=request.data)
        if serializer.is_valid():
            character = self.get_object()
            character_model = ContentType.objects.get_for_model(Person)
            serializer.save(
                content_type=character_model,
                object_id=character.pk,
            )
            return Response(
                {"detail": _("Picture uploaded successfully.")},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="voices",
    )
    def get_voices(self, request, *args, **kwargs):
        """
        Action retrieve characters associated with a voice actor.

        Endpoints:
        - GET api/v1/persons/{id}/voices/
        """
        author = self.get_object()
        characters = CharacterVoice.objects.filter(voice_id=author.pk)
        if characters.exists():
            serializer = CharacterVoiceReadSerializer(characters, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No relations found for this person."},
            status=status.HTTP_404_NOT_FOUND,
        )
