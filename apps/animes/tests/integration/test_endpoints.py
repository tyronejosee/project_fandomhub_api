"""Endpoint Tests for Animes App."""

import pytest
from datetime import timedelta
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APIClient

from apps.utils.functions import generate_test_image
from apps.characters.tests.factories import CharacterAnimeFactory
from apps.characters.serializers import CharacterMinimalSerializer
from apps.persons.tests.factories import PersonFactory, StaffAnimeFactory
from apps.persons.models import Person, StaffAnime
from apps.persons.serializers import StaffMinimalSerializer
from apps.producers.tests.factories import ProducerFactory
from apps.producers.choices import TypeChoices
from apps.reviews.tests.factories import ReviewFactory
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from apps.users.tests.factories import MemberFactory
from ...models import Anime
from ...choices import SeasonChoices


@pytest.mark.django_db
def test_list_animes(anonymous_user, anime):
    response = anonymous_user.get("/api/v1/animes/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_retrieve_anime(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert str(response.data["id"]) == str(anime.id)
    assert response.data["name"] == anime.name


@pytest.mark.django_db
def test_retrieve_anime_not_found(anonymous_user):
    response = anonymous_user.get(
        "/api/v1/genres/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_anime(contributor_user, genre, theme):
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


@pytest.mark.django_db
def test_create_anime_unauthorized(member_user):
    data = {}
    member_response = member_user.post("/api/v1/animes/", data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    member_user.logout()
    anonymus_response = member_user.post("/api/v1/animes/", data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_update_anime(contributor_user, anime, genre, theme):
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
        f"/api/v1/animes/{anime.id}/", data, format="multipart"
    )
    assert response.status_code == status.HTTP_200_OK
    anime.refresh_from_db()
    assert anime.name == "Updated Anime"


@pytest.mark.django_db
def test_partial_update_anime(contributor_user, anime):
    data = {"name": "Partially Updated Anime"}
    response = contributor_user.patch(
        f"/api/v1/animes/{anime.id}/",
        data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    anime.refresh_from_db()
    assert anime.name == "Partially Updated Anime"


@pytest.mark.django_db
def test_delete_anime(contributor_user, anime):
    assert anime.is_available
    response = contributor_user.delete(f"/api/v1/animes/{anime.id}/")
    anime.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Anime.objects.filter(id=anime.id).exists()
    assert not anime.is_available


@pytest.mark.django_db
def test_list_characters_by_anime(anonymous_user, anime, character):
    CharacterAnimeFactory(character_id=character, anime_id=anime)
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/characters/")
    assert response.status_code == status.HTTP_200_OK
    expected_data = CharacterMinimalSerializer([character], many=True).data
    assert response.json() == expected_data


@pytest.mark.django_db
def test_list_characters_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/characters/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "No characters found for this anime."


@pytest.mark.django_db
def test_list_staff_by_anime(anonymous_user, anime):
    staff_one = PersonFactory()
    staff_two = PersonFactory()
    StaffAnimeFactory(person_id=staff_one, anime_id=anime)
    StaffAnimeFactory(person_id=staff_two, anime_id=anime)
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/staff/")
    assert response.status_code == status.HTTP_200_OK
    staff_ids = StaffAnime.objects.filter(anime_id=anime.id).values_list(
        "person_id", flat=True
    )
    staff = Person.objects.filter(id__in=staff_ids)
    serializer = StaffMinimalSerializer(staff, many=True)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_list_staff_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/staff/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "No staff found for this anime."


@pytest.mark.django_db
def test_retrieve_stats_by_anime(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/stats/")
    assert response.status_code == status.HTTP_200_OK
    assert "id" in response.data
    assert "watching" in response.data
    assert "completed" in response.data
    assert "on_hold" in response.data
    assert "dropped" in response.data
    assert "plan_to_watch" in response.data
    assert "total" in response.data


@pytest.mark.django_db
def test_retrieve_stats_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(
        "/api/v1/animes/1ec14918-dbf8-41cd-b1fd-1ad4b4493835/stats/"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "Not found."


@pytest.mark.django_db
def test_list_reviews_by_anime(anonymous_user, anime):
    review = ReviewFactory(
        content_type=ContentType.objects.get_for_model(Anime),
        object_id=anime.id,
    )
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/reviews/")
    expected_data = ReviewReadSerializer([review], many=True).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_review_by_anime(member_user, anime, review):
    data = {
        "comment": "Review created",
        "is_spoiler": review.is_spoiler,
        "rating": review.rating,
    }
    response = member_user.post(
        f"/api/v1/animes/{anime.id}/reviews/create/",
        data,
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Review.objects.filter(comment="Review created").exists()
    assert response.data["comment"] == "Review created"


@pytest.mark.django_db
def test_update_review_by_anime(anime):
    user = MemberFactory()
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    review = ReviewFactory(
        user_id=user,
        content_type=ContentType.objects.get_for_model(Anime),
        object_id=anime.id,
    )
    data = {
        "comment": "Review updated",
        "is_spoiler": review.is_spoiler,
        "rating": review.rating,
    }
    response = api_client.patch(
        f"/api/v1/animes/{anime.id}/reviews/{review.id}/", data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    anime.refresh_from_db()
    assert response.data["comment"] == "Review updated"
