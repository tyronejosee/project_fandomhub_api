"""View Tests for Randoms App."""

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_random_anime_view(anonymous_user, anime):
    response = anonymous_user.get("/api/v1/random/anime/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0
    assert response.data["name"] == anime.name


@pytest.mark.django_db
def test_random_manga_view(anonymous_user, manga):
    response = anonymous_user.get("/api/v1/random/manga/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0
    assert response.data["name"] == manga.name


@pytest.mark.django_db
def test_random_character_view(anonymous_user, character):
    response = anonymous_user.get("/api/v1/random/character/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0
    assert response.data["name"] == character.name


@pytest.mark.django_db
def test_random_person_view(anonymous_user, person):
    response = anonymous_user.get("/api/v1/random/person/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0
    assert response.data["name"] == person.name
