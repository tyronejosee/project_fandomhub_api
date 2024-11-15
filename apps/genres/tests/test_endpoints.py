"""Factories for Genres Tests."""

import pytest


@pytest.mark.django_db
def test_genre_list(api_client, genre):
    response = api_client.get("/api/v1/genres/")

    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()["results"][0]["name"] == "Anime Genre"
