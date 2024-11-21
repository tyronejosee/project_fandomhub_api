"""ViewSet Tests for Animes App."""

import uuid
import pytest
from datetime import timedelta
from rest_framework import status


from apps.utils.functions import generate_test_image
from apps.producers.tests.factories import ProducerFactory
from apps.producers.choices import TypeChoices
from ..models import Anime
from ..choices import SeasonChoices


@pytest.mark.django_db
class TestAnimeViewSet:
    """Tests for AnimeViewSet API endpoints."""

    def test_list_animes(self, anonymous_user, anime):
        response = anonymous_user.get("/api/v1/animes/")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_retrieve_anime(self, anonymous_user, anime):
        response = anonymous_user.get(f"/api/v1/animes/{anime.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(response.data["id"]) == anime.id
        assert response.data["name"] == anime.name

    def test_retrieve_anime_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/genres/989423d1-d6c0-431a-8f62-d805b8a5f321/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_anime(self, contributor_user, genre, theme):
        producer = ProducerFactory(type=TypeChoices.STUDIO)
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "New Anime",
            "name_jpn": "New Anime",
            "image": image,
            "season": SeasonChoices.SPRING,
            "year": 2024,
            "aired_from": "2023-07-01",
            "studio_id": str(producer.id),
            "genres": [str(genre.id)],
            "themes": [str(theme.id)],
            "duration": timedelta(hours=1, minutes=45, seconds=30),
        }
        response = contributor_user.post(
            "/api/v1/animes/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert Anime.objects.filter(name="New Anime").exists()
        assert response.data["name"] == "New Anime"

    def test_create_anime_unauthorized(self, member_user):
        data = {"name": "Unauthorized Anime"}
        member_response = member_user.post("/api/v1/animes/", data, format="json")
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post("/api/v1/animes/", data, format="json")
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Anime.objects.filter(name="Unauthorized Anime").exists()

    def test_update_anime(self, contributor_user, anime, genre, theme):
        producer = ProducerFactory(type=TypeChoices.STUDIO)
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "Updated Anime",
            "name_jpn": "Updated Anime",
            "image": image,
            "season": SeasonChoices.SPRING,
            "year": 2024,
            "aired_from": "2023-07-01",
            "studio_id": str(producer.id),
            "genres": [str(genre.id)],
            "themes": [str(theme.id)],
            "duration": timedelta(hours=1, minutes=45, seconds=30),
        }
        response = contributor_user.put(
            f"/api/v1/animes/{anime.id}/",
            data,
            format="multipart",
        )

        assert response.status_code == status.HTTP_200_OK
        anime.refresh_from_db()
        assert anime.name == "Updated Anime"

    def test_partial_update_anime(self, contributor_user, anime):
        data = {"name": "Partially Updated Anime"}
        response = contributor_user.patch(
            f"/api/v1/animes/{anime.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        anime.refresh_from_db()
        assert anime.name == "Partially Updated Anime"

    def test_delete_anime(self, contributor_user, anime):
        assert anime.is_available

        response = contributor_user.delete(f"/api/v1/animes/{anime.id}/")
        anime.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Anime.objects.filter(id=anime.id).exists()
        assert not anime.is_available

    # ! TODO: Add tests for actions
