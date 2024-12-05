"""Endpoint Tests for Tops App."""

import pytest
from rest_framework import status

from apps.persons.choices import CategoryChoices
from apps.persons.tests.factories import PersonFactory
from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from apps.characters.tests.factories import CharacterFactory
from apps.reviews.tests.factories import ReviewFactory


@pytest.mark.django_db
def test_list_top_anime(anonymous_user):
    AnimeFactory.create_batch(3, favorites=10)
    endpoint = "/api/v1/top/animes/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 3
    assert all(anime["favorites"] == 10 for anime in response.data["results"])


@pytest.mark.django_db
def test_list_top_anime_errors(anonymous_user):
    endpoint = "/api/v1/top/animes/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No anime found."


@pytest.mark.django_db
def test_list_top_manga(anonymous_user):
    MangaFactory.create_batch(3, favorites=10)
    endpoint = "/api/v1/top/mangas/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 3
    assert all(manga["favorites"] == 10 for manga in response.data["results"])


@pytest.mark.django_db
def test_list_top_manga_errors(anonymous_user):
    endpoint = "/api/v1/top/mangas/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No manga found."


@pytest.mark.django_db
def test_list_top_character(anonymous_user):
    CharacterFactory.create_batch(3, favorites=10)
    endpoint = "/api/v1/top/characters/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 3
    assert all(character["favorites"] == 10 for character in response.data["results"])


@pytest.mark.django_db
def test_list_top_character_errors(anonymous_user):
    endpoint = "/api/v1/top/characters/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No character found."


@pytest.mark.django_db
def test_list_top_artist(anonymous_user):
    PersonFactory.create_batch(
        3,
        category=CategoryChoices.ARTIST,
        favorites=10,
    )
    endpoint = "/api/v1/top/artists/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 3
    assert all(artist["favorites"] == 10 for artist in response.data["results"])


@pytest.mark.django_db
def test_list_top_artist_errors(anonymous_user):
    endpoint = "/api/v1/top/artists/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No artists found."


@pytest.mark.django_db
def test_list_top_review(anonymous_user):
    ReviewFactory.create_batch(3, helpful_count=10)
    endpoint = "/api/v1/top/reviews/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 3
    assert all(review["helpful_count"] == 10 for review in response.data["results"])


@pytest.mark.django_db
def test_list_top_review_errors(anonymous_user):
    endpoint = "/api/v1/top/reviews/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No reviews found."
