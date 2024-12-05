"""Endpoint Tests for Recommendations App."""

import pytest
from rest_framework import status

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory


@pytest.mark.django_db
def test_list_anime_recommendation(anonymous_user):
    AnimeFactory.create_batch(3, is_recommended=True)
    endpoint = "/api/v1/recommendations/anime/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert response.data["count"] == 3
    assert len(response.data["results"]) == 3


@pytest.mark.django_db
def test_list_anime_recommendation_errors(anonymous_user):
    endpoint = "/api/v1/recommendations/anime/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert response.data["count"] == 0
    assert len(response.data["results"]) == 0


@pytest.mark.django_db
def test_list_manga_recommendation(anonymous_user):
    MangaFactory.create_batch(3, is_recommended=True)
    endpoint = "/api/v1/recommendations/manga/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert response.data["count"] == 3
    assert len(response.data["results"]) == 3


@pytest.mark.django_db
def test_list_manga_recommendation_errors(anonymous_user):
    endpoint = "/api/v1/recommendations/manga/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert response.data["count"] == 0
    assert len(response.data["results"]) == 0
