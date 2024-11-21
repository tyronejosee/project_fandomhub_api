"""View Tests for Tops App."""

import pytest
from rest_framework import status

from apps.persons.choices import CategoryChoices
from apps.persons.tests.factories import PersonFactory
from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from apps.characters.tests.factories import CharacterFactory
from apps.reviews.tests.factories import ReviewFactory


@pytest.mark.django_db
class TestTopAnimeView:

    def test_top_anime_list_success(self, anonymous_user):
        AnimeFactory.create_batch(3, favorites=10)
        response = anonymous_user.get("/api/v1/top/animes/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3
        assert all(anime["favorites"] == 10 for anime in response.data["results"])

    def test_top_anime_list_not_found(self, anonymous_user):
        response = anonymous_user.get("/api/v1/top/animes/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No anime found."


@pytest.mark.django_db
class TestTopMangaView:

    def test_top_manga_list_success(self, anonymous_user):
        MangaFactory.create_batch(3, favorites=10)
        response = anonymous_user.get("/api/v1/top/mangas/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3
        assert all(manga["favorites"] == 10 for manga in response.data["results"])

    def test_top_manga_list_not_found(self, anonymous_user):
        response = anonymous_user.get("/api/v1/top/mangas/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No manga found."


@pytest.mark.django_db
class TestTopCharacterView:

    def test_top_character_list_success(self, anonymous_user):
        CharacterFactory.create_batch(3, favorites=10)
        response = anonymous_user.get("/api/v1/top/characters/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3
        assert all(
            character["favorites"] == 10 for character in response.data["results"]
        )

    def test_top_character_list_not_found(self, anonymous_user):
        response = anonymous_user.get("/api/v1/top/characters/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No character found."


@pytest.mark.django_db
class TestTopArtistView:

    def test_top_artist_list_success(self, anonymous_user):
        PersonFactory.create_batch(
            3,
            category=CategoryChoices.ARTIST,
            favorites=10,
        )
        response = anonymous_user.get("/api/v1/top/artists/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3
        assert all(artist["favorites"] == 10 for artist in response.data["results"])

    def test_top_artist_list_not_found(self, anonymous_user):
        response = anonymous_user.get("/api/v1/top/artists/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No artists found."


@pytest.mark.django_db
class TestTopReviewView:

    def test_top_review_list_success(self, anonymous_user):
        ReviewFactory.create_batch(3, helpful_count=10)
        response = anonymous_user.get("/api/v1/top/reviews/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3
        assert all(review["helpful_count"] == 10 for review in response.data["results"])

    def test_top_review_list_not_found(self, anonymous_user):
        response = anonymous_user.get("/api/v1/top/reviews/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No reviews found."
