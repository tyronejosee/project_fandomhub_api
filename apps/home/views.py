"""Views for Home App."""

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view

from apps.animes.models import Anime
from apps.animes.choices import StatusChoices
from apps.animes.serializers import AnimeMinimalSerializer
from apps.animes.functions import get_current_season
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from .schemas import home_schemas


@extend_schema_view(**home_schemas)
class HomePageView(APIView):
    """View get all data for home page."""

    permission_classes = [AllowAny]
    cache_key = "home_data"

    def get(self, request, *args, **kwargs):
        cached_data = cache.get(self.cache_key)
        current_season, current_year = get_current_season()

        if cached_data is None:
            # Queries
            # TODO: add most_popular_anime_trailers
            # TODO: add anime_and_manga_news
            # TODO: add featured_articles
            current_season = Anime.objects.filter(
                status=StatusChoices.AIRING,
                season=current_season,
                year=current_year,
            )[:25]
            latest_anime_reviews = Review.objects.filter(
                content_type__model="anime"
            ).order_by("-created_at")[:25]
            latest_anime_recommendations = Anime.objects.filter(
                is_recommended=True
            ).order_by("-created_at")[:8]

            # Data serialized
            current_season_serialized = AnimeMinimalSerializer(
                current_season, many=True
            )
            anime_reviews_serialized = ReviewReadSerializer(
                latest_anime_reviews, many=True
            )
            anime_recommendations_serialized = AnimeMinimalSerializer(
                latest_anime_recommendations, many=True
            )

            # JSON data
            data = {
                "current_season": current_season_serialized.data,
                "anime_reviews": anime_reviews_serialized.data,
                "anime_recommendations": anime_recommendations_serialized.data,
            }

            cache.set(self.cache_key, data, 7200)  # 2 hrs.
            return Response(data)

        return Response(cached_data)
