"""Schemas for Animes App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

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
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    "create": extend_schema(
        summary="Create Anime",
        description="Create a new anime, only for `IsContributor` or `IsAdministrator` users.",
        request=AnimeWriteSerializer,
        responses={
            201: OpenApiResponse(AnimeWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["animes"],
    ),
    "retrieve": extend_schema(
        summary="Get Anime",
        description="Get detailed information about a specific anime.",
        responses={
            200: OpenApiResponse(AnimeReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    "update": extend_schema(
        summary="Update Anime",
        description="Update all fields of a specific anime, only for `IsContributor` or `IsAdministrator` users.",
        request=AnimeWriteSerializer,
        responses={
            200: OpenApiResponse(AnimeWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["animes"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update Anime",
        description="Update some fields of a specific anime, only for `IsContributor` or `IsAdministrator` users.",
        request=AnimeWriteSerializer,
        responses={
            200: OpenApiResponse(AnimeWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["animes"],
    ),
    "destroy": extend_schema(
        summary="Remove Anime",
        description="Remove a specific anime, only for `IsContributor` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["animes"],
    ),
    "get_characters": extend_schema(
        summary="Get Anime Characters",
        description="Get all characters of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(CharacterMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    # "get_episodes": extend_schema(),
    "get_staff": extend_schema(
        summary="Get Anime Staff",
        description="Get all staff of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(StaffMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    "get_stats": extend_schema(
        summary="Get Anime Stats",
        description="Get statistics of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeStatsReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    "get_reviews": extend_schema(
        summary="Get Anime Reviews",
        description="Get reviews of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(ReviewReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    "create_review": extend_schema(
        summary="Create Anime Review",
        description="Create a new review for anime, only for `IsMember`",
        request=ReviewWriteSerializer,
        responses={
            201: OpenApiResponse(ReviewWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["animes"],
    ),
    "update_or_delete_review": extend_schema(
        summary="Partial Update or Remove Anime Review",
        description="Update some fields or delete of a anime, only for `IsMember` or `IsAdministrator` users.",
        request=ReviewWriteSerializer,
        responses={
            200: OpenApiResponse(ReviewWriteSerializer, description="OK"),
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        parameters=[OpenApiParameter("review_id", str, OpenApiParameter.PATH)],
        methods=["PATCH", "DELETE"],
        tags=["animes"],
    ),
    "get_recommendations": extend_schema(
        summary="Get Anime Recommendations",
        description="Get recommendations of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    # "get_interest_stacks": extend_schema(),
    "get_news": extend_schema(
        summary="Get Anime News",
        description="Get news of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(NewsMinimalSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    # "get_forum": extend_schema(),
    # "get_clubs": extend_schema(),
    "get_videos": extend_schema(
        summary="Get Anime Videos",
        description="Get videos of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(VideoReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
    "get_pictures": extend_schema(
        summary="Get Anime Pictures",
        description="Get pictures of the anime passed as param (`uuid`).",
        responses={
            200: OpenApiResponse(PictureReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["animes"],
    ),
}


schedule_schemas = {
    "get": extend_schema(
        summary="Get Schedules",
        description="Get anime calendar or schedule for the current season.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["schedules"],
    ),
}


season_anime_schemas = {
    "get": extend_schema(
        summary="Get Season Anime",
        description="Get animes filtered by year and season.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["seasons"],
    ),
}


current_season_anime_schemas = {
    "get": extend_schema(
        summary="Get Current Season Anime",
        description="Get animes of the current season.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["seasons"],
    ),
}


upcomming_season_anime_schemas = {
    "get": extend_schema(
        summary="Get Upcomming Season Anime",
        description="Get animes of the upcoming season.",
        responses={
            200: OpenApiResponse(AnimeMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["seasons"],
    ),
}
