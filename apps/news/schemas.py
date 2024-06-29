"""Schemas for News App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import NewsReadSerializer, NewsWriteSerializer, NewsMinimalSerializer


news_schemas = {
    "list": extend_schema(
        summary="Get Several News",
        description="Get a list of available news.",
        responses={
            200: OpenApiResponse(NewsMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "create": extend_schema(
        summary="Create News",
        description="Create a news, only for `IsModerator` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(NewsWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get News",
        description="Get detailed information about a specific news.",
        responses={
            200: OpenApiResponse(NewsReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "update": extend_schema(
        summary="Update News",
        description="Update all fields of a specific news, only for `IsModerator` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(NewsWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update News",
        description="Update some fields of a specific news, only for `IsModerator` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(NewsWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove News",
        description="Remove a specific news, only for `IsModerator` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
}
