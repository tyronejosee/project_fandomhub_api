"""Schemas for Profiles App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.serializers import CharacterReadSerializer
from apps.persons.serializers import PersonReadSerializer


random_anime_schemas = {
    "get": extend_schema(
        summary="Get Random Anime",
        description="Retrieve a random anime from the entire available catalog.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
        },
        auth=[],
        tags=["randoms"],
    ),
}


random_manga_schemas = {
    "get": extend_schema(
        summary="Get Random Manga",
        description="Retrieve a random manga from the entire available catalog.",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
        },
        auth=[],
        tags=["randoms"],
    ),
}


random_character_schemas = {
    "get": extend_schema(
        summary="Get Random Character",
        description="Retrieve a random character from the entire available catalog.",
        responses={
            200: OpenApiResponse(CharacterReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
        },
        auth=[],
        tags=["randoms"],
    ),
}


random_person_schemas = {
    "get": extend_schema(
        summary="Get Random Person",
        description="Retrieve a random person from the entire available catalog.",
        responses={
            200: OpenApiResponse(PersonReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
        },
        auth=[],
        tags=["randoms"],
    ),
}
