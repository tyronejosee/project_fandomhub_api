"""Schemas for Tops App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from apps.characters.serializers import CharacterMinimalSerializer
from apps.persons.serializers import PersonMinimalSerializer
from apps.reviews.serializers import ReviewReadSerializer


top_anime_schemas = {
    "get": extend_schema(
        summary="Get Top Animes",
        description="Get a list of top animes.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}


top_manga_schemas = {
    "get": extend_schema(
        summary="Get Top Mangas",
        description="Get a list of top mangas.",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer(many=True), description="OK"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}


top_character_schemas = {
    "get": extend_schema(
        summary="Get Top Characters",
        description="Get a list of top characters.",
        responses={
            200: OpenApiResponse(
                CharacterMinimalSerializer(many=True), description="OK"
            ),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}


top_artist_schemas = {
    "get": extend_schema(
        summary="Get Top Artists",
        description="Get a list of top artists.",
        responses={
            200: OpenApiResponse(PersonMinimalSerializer(many=True), description="OK"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}


top_review_schemas = {
    "get": extend_schema(
        summary="Get Top Reviews",
        description="Get a list of top reviews.",
        responses={
            200: OpenApiResponse(ReviewReadSerializer(many=True), description="OK"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}
