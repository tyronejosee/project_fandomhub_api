"""View Tests for Recommendations App."""

import pytest
from rest_framework import status

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory


@pytest.mark.django_db
def test_anime_recommendation_view_success(anonymous_user):
    AnimeFactory.create_batch(3, is_recommended=True)
    response = anonymous_user.get("/api/v1/recommendations/anime/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 3
    assert len(response.data["results"]) == 3


@pytest.mark.django_db
def test_anime_recommendation_view_not_found(anonymous_user):
    response = anonymous_user.get("/api/v1/recommendations/anime/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 0
    assert len(response.data["results"]) == 0


@pytest.mark.django_db
def test_manga_recommendation_view_success(anonymous_user):
    MangaFactory.create_batch(3, is_recommended=True)
    response = anonymous_user.get("/api/v1/recommendations/manga/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 3
    assert len(response.data["results"]) == 3


@pytest.mark.django_db
def test_manga_recommendation_view_not_found(anonymous_user):
    response = anonymous_user.get("/api/v1/recommendations/manga/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 0
    assert len(response.data["results"]) == 0
