"""Schemas for Producers App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.animes.serializers import AnimeMinimalSerializer
from .serializers import ProducerReadSerializer, ProducerWriteSerializer


producer_schemas = {
    "list": extend_schema(
        summary="Get Several Producers",
        description="Get a list of available producers.",
        responses={
            200: OpenApiResponse(ProducerReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["producers"],
    ),
    "create": extend_schema(
        summary="Create Producer",
        description="Create a producer, only for `IsContributor` or `IsAdministrator` users.",
        request=ProducerWriteSerializer,
        responses={
            201: OpenApiResponse(ProducerWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["producers"],
    ),
    "retrieve": extend_schema(
        summary="Get Producer",
        description="Get detailed information about a specific producer.",
        responses={
            200: OpenApiResponse(ProducerReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["producers"],
    ),
    "update": extend_schema(
        summary="Update Producer",
        description="Update all fields of a specific producer, only for `IsContributor` or `IsAdministrator` users.",
        request=ProducerWriteSerializer,
        responses={
            200: OpenApiResponse(ProducerWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["producers"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update Producer",
        description="Update some fields of a specific producer, only for `IsContributor` or `IsAdministrator` users.",
        request=ProducerWriteSerializer,
        responses={
            200: OpenApiResponse(ProducerWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["producers"],
    ),
    "destroy": extend_schema(
        summary="Remove Producer",
        description="Remove a specific producer, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["producers"],
    ),
    "get_animes": extend_schema(
        summary="Get Producer Animes",
        description="Get all animes of an producer passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["producers"],
    ),
}
