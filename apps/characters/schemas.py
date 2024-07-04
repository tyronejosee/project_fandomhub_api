"""Schemas for Characters App"""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.utils.serializers import PictureReadSerializer, PictureWriteSerializer
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from apps.persons.serializers import PersonMinimalSerializer
from .serializers import CharacterReadSerializer, CharacterWriteSerializer


character_schemas = {
    "list": extend_schema(
        summary="Get Several Characters",
        description="Get a list of available characters.",
        responses={
            200: OpenApiResponse(CharacterReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "create": extend_schema(
        summary="Create Character",
        description="Create a new character, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(CharacterWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Character",
        description="Get detailed information about a specific character.",
        responses={
            200: OpenApiResponse(CharacterReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "update": extend_schema(
        summary="Update Character",
        description="Update all fields of a specific character, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(CharacterWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Character",
        description="Update some fields of a specific character, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(CharacterWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Character",
        description="Remove a specific character, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "get_pictures": extend_schema(
        summary="Get Character Pictures",
        description="Get all pictures of an character passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(PictureReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "create_picture": extend_schema(
        summary="Create Character Picture",
        description="Create a new picture for character, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(PictureWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "get_voices": extend_schema(
        summary="Get Character Voices",
        description="Get all voices of an character passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(PersonMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "get_anime": extend_schema(
        summary="Get Character Anime",
        description="Get anime of an character passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "get_manga": extend_schema(
        summary="Get Character Manga",
        description="Get manga of an character passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}
