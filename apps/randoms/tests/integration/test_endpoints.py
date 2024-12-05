"""Endpoint Tests for Randoms App."""

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_retrive_random_anime(anonymous_user, anime):
    endpoint = "/api/v1/random/anime/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0
    assert response.data["name"] == anime.name


@pytest.mark.django_db
def test_retrive_random_anime_errors(anonymous_user):
    endpoint = "/api/v1/random/anime/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No available content found."


@pytest.mark.django_db
def test_retrieve_random_manga(anonymous_user, manga):
    endpoint = "/api/v1/random/manga/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0
    assert response.data["name"] == manga.name


@pytest.mark.django_db
def test_retrieve_random_manga_errors(anonymous_user):
    endpoint = "/api/v1/random/manga/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No available content found."


@pytest.mark.django_db
def test_retrieve_random_character(anonymous_user, character):
    endpoint = "/api/v1/random/character/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0
    assert response.data["name"] == character.name


@pytest.mark.django_db
def test_retrieve_random_character_errors(anonymous_user):
    endpoint = "/api/v1/random/character/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No available content found."


@pytest.mark.django_db
def test_retrieve_random_person(anonymous_user, person):
    endpoint = "/api/v1/random/person/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0
    assert response.data["name"] == person.name


@pytest.mark.django_db
def test_retrieve_random_person_errors(anonymous_user):
    endpoint = "/api/v1/random/person/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No available content found."
