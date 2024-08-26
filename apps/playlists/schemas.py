"""Schemas for Playlists App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

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


animelist_schemas = {
    "get": extend_schema(
        summary="Get Animelist",
        description="Get detailed information about a specific animelist.",
        responses={
            200: OpenApiResponse(AnimeListReadSerializer, description="OK"),
        },
        tags=["animelists"],
    ),
    "patch": extend_schema(
        summary="Update Animelist",
        description="Update some fields of a animelist, only for `IsMember` users.",
        request=AnimeListWriteSerializer,
        responses={
            200: OpenApiResponse(AnimeListWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            500: OpenApiResponse(description="Internal Server Error"),
        },
        tags=["animelists"],
    ),
}


animelist_item_schemas = {
    "get": extend_schema(
        summary="Get Animes from Animelist",
        description="Get all animes of the animelist, only creator (`IsMember`).",
        responses={
            200: OpenApiResponse(AnimeListItemReadSerializer, description="OK"),
            204: OpenApiResponse(description="No Content"),
        },
        tags=["animelists"],
    ),
    "post": extend_schema(
        summary="Create Anime in Animelist",
        description="Create an anime in the animelist, only creator (`IsMember`).",
        request=AnimeListItemWriteSerializer,
        responses={
            201: OpenApiResponse(AnimeListItemWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            500: OpenApiResponse(description="Internal Server Error"),
        },
        tags=["animelists"],
    ),
}


animelist_item_detail_schemas = {
    "get": extend_schema(
        summary="Get Anime from Animelist",
        description="Get a specific anime from the animelist, only creator (`IsMember`).",
        responses={
            200: OpenApiResponse(AnimeListItemReadSerializer, description="OK"),
        },
        tags=["animelists"],
    ),
    "patch": extend_schema(
        summary="Update Anime from Animelist",
        description="Update specific fields of an anime in the animelist, only creator (`IsMember`).",
        request=AnimeListItemWriteSerializer,
        responses={
            200: OpenApiResponse(AnimeListItemWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
        },
        tags=["animelists"],
    ),
    "delete": extend_schema(
        summary="Remove Anime from Animelist",
        description="Remove an anime from the animelist, only creator (`IsMember`).",
        responses={
            204: OpenApiResponse(description="No Content"),
        },
        tags=["animelists"],
    ),
}


mangalist_schemas = {
    "get": extend_schema(
        summary="Get Mangalist",
        description="Get detailed information about a specific mangalist.",
        responses={
            200: OpenApiResponse(MangaListReadSerializer, description="OK"),
        },
        tags=["mangalists"],
    ),
    "patch": extend_schema(
        summary="Update Mangalist",
        description="Update some fields of a mangalist, only for `IsMember` users.",
        request=MangaListWriteSerializer,
        responses={
            200: OpenApiResponse(MangaListWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            500: OpenApiResponse(description="Internal Server Error"),
        },
        tags=["mangalists"],
    ),
}


mangalist_item_schemas = {
    "get": extend_schema(
        summary="Get Mangas from Mangalist",
        description="Get all mangas of the mangalist, only creator (`IsMember`).",
        responses={
            200: OpenApiResponse(MangaListItemReadSerializer, description="OK"),
            204: OpenApiResponse(description="No Content"),
        },
        tags=["mangalists"],
    ),
    "post": extend_schema(
        summary="Create Manga in Mangalist",
        description="Create an manga in the mangalist, only creator (`IsMember`).",
        request=MangaListItemWriteSerializer,
        responses={
            201: OpenApiResponse(MangaListItemWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            500: OpenApiResponse(description="Internal Server Error"),
        },
        tags=["mangalists"],
    ),
}


mangalist_item_detail_schemas = {
    "get": extend_schema(
        summary="Get Manga from Mangalist",
        description="Get a specific manga from the mangalist, only creator (`IsMember`).",
        responses={
            200: OpenApiResponse(MangaListItemReadSerializer, description="OK"),
        },
        tags=["mangalists"],
    ),
    "patch": extend_schema(
        summary="Update Manga from Mangalist",
        description="Update specific fields of an manga in the mangalist, only creator (`IsMember`).",
        request=MangaListItemWriteSerializer,
        responses={
            200: OpenApiResponse(MangaListItemWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
        },
        tags=["mangalists"],
    ),
    "delete": extend_schema(
        summary="Remove Maga from Mangalist",
        description="Remove an manga from the mangalist, only creator (`IsMember`).",
        responses={
            204: OpenApiResponse(description="No Content"),
        },
        tags=["mangalists"],
    ),
}
