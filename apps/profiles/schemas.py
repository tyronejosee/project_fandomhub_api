"""Schemas for Profiles App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    ProfileReadSerializer,
    ProfileWriteSerializer,
    ProfileMinimalSerializer,
)


profile_schemas = {
    "list": extend_schema(
        summary="Get Several Profiles",
        description="Get a list of available profiles.",
        responses={
            200: OpenApiResponse(ProfileMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["profiles"],
    ),
    "create": extend_schema(
        summary="Create Profile",
        description="Create a new profile, only for `IsAdministrator` users.",
        request=ProfileWriteSerializer,
        responses={
            201: OpenApiResponse(ProfileWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["profiles"],
    ),
    "retrieve": extend_schema(
        summary="Get Profile",
        description="Get detailed information about a specific profile.",
        responses={
            200: OpenApiResponse(ProfileReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["profiles"],
    ),
    "update": extend_schema(
        summary="Update Profile",
        description="Update all fields of a specific profile, only for `IsAdministrator` users.",
        request=ProfileWriteSerializer,
        responses={
            200: OpenApiResponse(ProfileWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["profiles"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update Profile",
        description="Update some fields of a specific profile, only for `IsAdministrator` users.",
        request=ProfileWriteSerializer,
        responses={
            200: OpenApiResponse(ProfileWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["profiles"],
    ),
    "destroy": extend_schema(
        summary="Remove Profile",
        description="Remove a specific profile, only for `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["profiles"],
    ),
    "get_my_profile": extend_schema(
        summary="Get User Profile",
        description="Get user profile, only creator (`IsMember`).",
        responses={
            200: OpenApiResponse(ProfileReadSerializer, description="OK"),
        },
        tags=["profiles"],
    ),
    "update_user_profile": extend_schema(
        summary="Update User Profile",
        description="Update some fields of a user profile, only creator (`IsMember`).",
        request=ProfileWriteSerializer,
        responses={
            200: OpenApiResponse(ProfileWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
        },
        tags=["profiles"],
    ),
}
