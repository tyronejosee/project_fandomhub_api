"""Endpoint Tests for Animes App."""

import uuid
import pytest


@pytest.mark.django_db
def test_anime_list(api_client, anime):
    response = api_client.get("/api/v1/animes/")

    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_anime_detail(api_client, anime):
    response = api_client.get(f"/api/v1/animes/{anime.id}/")
    data = response.json()

    assert response.status_code == 200
    assert uuid.UUID(data["id"]) == anime.id
    assert data["name"] == anime.name
