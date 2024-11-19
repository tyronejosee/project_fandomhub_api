"""View Tests for Home App."""

# import pytest
# from django.core.cache import cache
# from rest_framework import status
# from datetime import datetime

# from apps.animes.tests.factories import AnimeFactory
# from apps.reviews.tests.factories import ReviewFactory


# @pytest.mark.django_db
# class TestHomePageView:

#     @pytest.fixture
#     def setup_data(self):
#         """Create sample data using Factory Boy."""
#         current_year = datetime.now().year
#         current_season = "fall"

#         # Create sample animes for the current season
#         current_season_animes = AnimeFactory.create_batch(
#             30,
#             season=current_season,
#             year=current_year,
#         )

#         # Create sample anime reviews
#         reviews = ReviewFactory.create_batch(30)

#         # Create sample recommended animes
#         recommended_animes = AnimeFactory.create_batch(10, is_recommended=True)

#         return {
#             "current_season_animes": current_season_animes,
#             "reviews": reviews,
#             "recommended_animes": recommended_animes,
#         }

#     def test_returns_cached_data(self, anonymous_user, setup_data):
#         """Test that cached data is returned if available."""
#         cache_key = "home_data"
#         cached_data = {
#             "current_season": [{"name": "Cached Anime"}],
#             "anime_reviews": [{"comment": "Cached Review"}],
#             "anime_recommendations": [{"name": "Cached Recommendation"}],
#         }
#         cache.set(cache_key, cached_data, 7200)  # Set cached data

#         response = anonymous_user.get("api/v1/home/")

#         assert response.status_code == status.HTTP_200_OK
#         assert response.json() == cached_data

#     def test_generates_and_caches_data(self, anonymous_user, setup_data):
#         """Test that the view generates and caches data if cache is empty."""
#         cache_key = "home_data"
#         cache.clear()  # Clear any existing cache

#         response = anonymous_user.get("api/v1/home/")

#         assert response.status_code == status.HTTP_200_OK

#         # Check the response structure
#         data = response.json()
#         assert "current_season" in data
#         assert "anime_reviews" in data
#         assert "anime_recommendations" in data

#         # Verify that cache is populated
#         cached_data = cache.get(cache_key)
#         assert cached_data == data

#         # Verify data lengths
#         assert len(data["current_season"]) == 25  # Limited to 25
#         assert len(data["anime_reviews"]) == 25  # Limited to 25
#         assert len(data["anime_recommendations"]) == 8  # Limited to 8
