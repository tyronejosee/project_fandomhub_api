"""Schemas for Home App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer

from apps.animes.serializers import AnimeMinimalSerializer
from apps.reviews.serializers import ReviewReadSerializer

HomePageResponseSerializer = inline_serializer(
    name="HomePageResponse",
    fields={
        "current_season": AnimeMinimalSerializer(many=True),
        "anime_reviews": ReviewReadSerializer(many=True),
        "anime_recommendations": AnimeMinimalSerializer(many=True),
    },
)

home_schemas = {
    "get": extend_schema(
        summary="Get Home Page Data",
        description="List of anime data for the current season, latest reviews, and recommendations.",
        responses={
            200: OpenApiResponse(
                response=HomePageResponseSerializer,
                description="OK",
            ),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["home"],
    ),
}
