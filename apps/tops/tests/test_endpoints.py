"""Endpoint Tests for Tops App."""

import pytest

from apps.animes.tests.factories import AnimeFactory


@pytest.mark.django_db
class TestTopAnimeEndpoints:

    def test_top_anime_list_success(self, anonymous_user):
        AnimeFactory.create_batch(5, favorites=10)
        response = anonymous_user.get("/api/v1/top/animes/")

        assert response.status_code == 200
        data = response.json()
        assert len(data["results"]) == 5
        assert all(anime["favorites"] == 10 for anime in data["results"])
