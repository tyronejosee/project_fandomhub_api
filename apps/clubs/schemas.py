"""Schemas for Clubs App"""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    ClubReadSerializer,
    ClubWriteSerializer,
    ClubMemberReadSerializer,
)

club_schemas = {
    "list": extend_schema(
        summary="Get Several Clubs",
        description="Get a list of available clubs.",
        responses={
            200: OpenApiResponse(ClubReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["clubs"],
    ),
    "create": extend_schema(
        summary="Create Club",
        description="Create a new club, only for `IsMember` or `IsAdministrator` users.",
        request=ClubWriteSerializer,
        responses={
            201: OpenApiResponse(ClubWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["clubs"],
    ),
    "retrieve": extend_schema(
        summary="Get Club",
        description="Get detailed information about a specific club.",
        responses={
            200: OpenApiResponse(ClubReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["clubs"],
    ),
    "update": extend_schema(
        summary="Update Club",
        description="Update all fields of a specific club, only for `IsMember` or `IsAdministrator` users.",
        request=ClubWriteSerializer,
        responses={
            200: OpenApiResponse(ClubWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["clubs"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update Club",
        description="Update some fields of a specific club, only for `IsMember` or `IsAdministrator` users.",
        request=ClubWriteSerializer,
        responses={
            200: OpenApiResponse(ClubWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["clubs"],
    ),
    "destroy": extend_schema(
        summary="Remove Club",
        description="Remove a specific club, only for `IsMember` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["clubs"],
    ),
    "get_members": extend_schema(
        summary="Get Club Members",
        description="Get all members of an club passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(ClubMemberReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["clubs"],
    ),
}
