"""Schemas for Animes App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.utils.serializers import PictureReadSerializer, VideoReadSerializer
from apps.characters.serializers import CharacterMinimalSerializer
from apps.persons.serializers import StaffMinimalSerializer
from apps.news.serializers import NewsMinimalSerializer
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from .serializers import (
    AnimeReadSerializer,
    AnimeWriteSerializer,
    AnimeMinimalSerializer,
    AnimeStatsReadSerializer,
)


anime_schemas = {
    "list": extend_schema(
        summary="Get Several Animes",
        description="Get a list of the entire catalog of available anime.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "create": extend_schema(
        summary="Create Anime",
        description="Create a new anime, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            201: OpenApiResponse(AnimeWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "retrieve": extend_schema(
        summary="Get Anime",
        description="Get detailed information about a specific anime.",
        responses={
            200: OpenApiResponse(AnimeReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "update": extend_schema(
        summary="Update Anime",
        description="Update all fields of a specific anime, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(AnimeWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "partial_update": extend_schema(
        summary="Partial Update Anime",
        description="Update some fields of a specific anime, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(AnimeWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "destroy": extend_schema(
        summary="Remove Anime",
        description="Remove a specific anime, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
    ),
    "get_characters": extend_schema(
        summary="Get Anime Characters",
        description="Get all characters of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(CharacterMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    # "get_episodes": extend_schema(),
    "get_staff": extend_schema(
        summary="Get Anime Staff",
        description="Get all staff of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(StaffMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "get_stats": extend_schema(
        summary="Get Anime Stats",
        description="Get statistics of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeStatsReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "get_reviews": extend_schema(
        summary="Get Anime Reviews",
        description="Get reviews of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(ReviewReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "create_review": extend_schema(
        summary="Create Anime Review",
        description="Create a new review for anime, only for `IsMember`",
        responses={
            201: OpenApiResponse(ReviewWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
    ),
    "update_or_delete_review": extend_schema(
        summary="Partial Update or Remove Anime",
        description="Update some fields or delete of a anime, only for `IsMember` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(ReviewWriteSerializer, description="OK"),
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        methods=["PATCH", "DELETE"],
    ),
    "get_recommendations": extend_schema(
        summary="Get Anime Recommendations",
        description="Get recommendations of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    # "get_interest_stacks": extend_schema(),
    "get_news": extend_schema(
        summary="Get Anime News",
        description="Get news of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(NewsMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    # "get_forum": extend_schema(),
    # "get_clubs": extend_schema(),
    "get_videos": extend_schema(
        summary="Get Anime Videos",
        description="Get videos of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(VideoReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
    "get_pictures": extend_schema(
        summary="Get Anime Pictures",
        description="Get pictures of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(PictureReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
    ),
}
