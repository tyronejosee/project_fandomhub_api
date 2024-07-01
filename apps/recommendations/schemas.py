"""Schemas for Recommendations App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer


anime_recommendation_schemas = {
    "get": extend_schema(
        summary="Get Anime Recommendations",
        description="Get a list of anime recommendations created by the admins.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
        },
        auth=[],
    ),
}


manga_recommendation_schemas = {
    "get": extend_schema(
        summary="Get Manga Recommendations",
        description="Get a list of manga recommendations created by the admins.",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
        },
        auth=[],
    ),
}
