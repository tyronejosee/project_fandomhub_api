"""Schemas for Mangas App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.utils.serializers import PictureReadSerializer
from apps.characters.serializers import CharacterMinimalSerializer
from apps.news.serializers import NewsMinimalSerializer
from .serializers import (
    MagazineReadSerializer,
    MagazineWriteSerializer,
    MangaReadSerializer,
    MangaWriteSerializer,
    MangaMinimalSerializer,
    MangaStatsReadSerializer,
)


magazine_schemas = {
    "list": extend_schema(
        summary="Get Several Magazines",
        description="Get a list of available magazines.",
        responses={
            200: OpenApiResponse(MagazineReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "create": extend_schema(
        summary="Create Magazine",
        description="Create a new magazine, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(MagazineWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Magazine",
        description="Get detailed information about a specific magazine.",
        responses={
            200: OpenApiResponse(MagazineReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]

    ),
    "update": extend_schema(
        summary="Update Magazine",
        description="Update all fields of a specific magazine, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(MagazineWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Magazine",
        description="Update some fields of a specific magazine, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(MagazineWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Magazine",
        description="Remove a specific magazine, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    )
}


manga_schemas = {
    "list": extend_schema(
        summary="Get Several Mangas",
        description="Get a list of available mangas.",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "create": extend_schema(
        summary="Create Manga",
        description="Create a new manga, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(MangaWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Manga",
        description="Get detailed information about a specific manga.",
        responses={
            200: OpenApiResponse(MangaReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]

    ),
    "update": extend_schema(
        summary="Update Manga",
        description="Update all fields of a specific manga, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(MangaWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Manga",
        description="Update some fields of a specific manga, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(MangaWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Manga",
        description="Remove a specific manga, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "get_characters": extend_schema(
        summary="Get Manga Characters",
        description="Get all characters of an manga passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(CharacterMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "get_stats": extend_schema(
        summary="Get Manga Stats",
        description="Get all stats of an manga passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(MangaStatsReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    # TODO: Add schema for review_list, pending refactor
    # TODO: Add schema for review_detail and review_id param, pending refactor
    "get_recommendations": extend_schema(
        summary="Get Manga Recommendations",
        description="Get all recommendations of an manga passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "get_news": extend_schema(
        summary="Get Manga News",
        description="Get all news of an manga passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(NewsMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    # "get_forum": extend_schema(),
    "get_pictures": extend_schema(
        summary="Get Manga Pictures",
        description="Get all pictures of an manga passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(PictureReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    )
}
