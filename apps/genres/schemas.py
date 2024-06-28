"""Schemas for Genres App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.serializers import MangaMinimalSerializer
from .serializers import (
    GenreReadSerializer,
    GenreWriteSerializer,
    ThemeReadSerializer,
    ThemeWriteSerializer,
    DemographicReadSerializer,
    DemographicWriteSerializer,
)


genre_schemas = {
    "list": extend_schema(
        summary="Get Several Genres",
        description="Get a list of available genres.",
        responses={
            200: OpenApiResponse(GenreReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "create": extend_schema(
        summary="Create Genre",
        description="Create a new genre, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(GenreWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Genre",
        description="Get detailed information about a specific genre.",
        responses={
            200: OpenApiResponse(GenreReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]

    ),
    "update": extend_schema(
        summary="Update Genre",
        description="Update all fields of a specific genre, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(GenreWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Genre",
        description="Update some fields of a specific genre, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(GenreWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Genre",
        description="Remove a specific genre, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "get_animes": extend_schema(
        summary="Get Genre Animes",
        description="Get all animes of an genre passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "get_mangas": extend_schema(
        summary="Get Genre Mangas",
        description="Get all mangas of an genre passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(MangaMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
}


theme_schemas = {
    "list": extend_schema(
        summary="Get Several Themes",
        description="Get a list of available themes.",
        responses={
            200: OpenApiResponse(ThemeReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "create": extend_schema(
        summary="Create Theme",
        description="Create a new theme, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(ThemeWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Theme",
        description="Get detailed information about a specific theme.",
        responses={
            200: OpenApiResponse(ThemeReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]

    ),
    "update": extend_schema(
        summary="Update Theme",
        description="Update all fields of a specific theme, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(ThemeWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Theme",
        description="Update some fields of a specific theme, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(ThemeWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Theme",
        description="Remove a specific theme, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    )
}


demographic_schemas = {
    "list": extend_schema(
        summary="Get Several Demographics",
        description="Get a list of available demographics.",
        responses={
            200: OpenApiResponse(DemographicReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]
    ),
    "create": extend_schema(
        summary="Create Demographic",
        description="Create a new demographic, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(DemographicWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Demographic",
        description="Get detailed information about a specific demographic.",
        responses={
            200: OpenApiResponse(DemographicReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found")
        },
        auth=[]

    ),
    "update": extend_schema(
        summary="Update Demographic",
        description="Update all fields of a specific demographic, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(DemographicWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Demographic",
        description="Update some fields of a specific demographic, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(DemographicWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Demographic",
        description="Remove a specific demographic, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    )
}
