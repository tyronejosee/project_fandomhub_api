"""Endpoint Tests for Animes App."""

import pytest
from datetime import timedelta
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APIClient

from apps.characters.tests.factories import CharacterAnimeFactory
from apps.news.tests.factories import NewsFactory
from apps.persons.tests.factories import PersonFactory, StaffAnimeFactory
from apps.persons.models import Person, StaffAnime
from apps.persons.serializers import StaffMinimalSerializer
from apps.producers.tests.factories import ProducerFactory
from apps.producers.choices import TypeChoices
from apps.reviews.tests.factories import ReviewFactory
from apps.reviews.models import Review
from apps.users.tests.factories import MemberFactory
from apps.utils.functions import generate_test_image
from apps.utils.tests.factories import VideoFactory, PictureFactory
from ...models import Anime
from ...choices import SeasonChoices
from ..factories import AnimeFactory


@pytest.mark.django_db
def test_list_animes(anonymous_user, anime):
    response = anonymous_user.get("/api/v1/animes/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0


@pytest.mark.django_db
def test_list_animes_errors(anonymous_user):
    response = anonymous_user.get("/api/v1/animes/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    # TODO: Update status code to 404


@pytest.mark.django_db
def test_retrieve_anime(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(anime.id)
    assert response.data["name"] == anime.name


@pytest.mark.django_db
def test_retrieve_anime_errors(anonymous_user):
    anime_id = "989423d1-d6c0-431a-8f62-d805b8a5f321"
    response = anonymous_user.get(f"/api/v1/animes/{anime_id}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"


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
    response = contributor_user.post("/api/v1/animes/", data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Anime.objects.filter(name="New Anime").exists()
    assert response.data["name"] == "New Anime"


@pytest.mark.django_db
def test_create_anime_errors(member_user):
    data = {}
    member_response = member_user.post("/api/v1/animes/", data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post("/api/v1/animes/", data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"


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
    assert response.reason_phrase == "OK"
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
    assert response.reason_phrase == "OK"
    anime.refresh_from_db()
    assert anime.name == "Partially Updated Anime"


@pytest.mark.django_db
def test_delete_anime(contributor_user, anime):
    assert anime.is_available
    response = contributor_user.delete(f"/api/v1/animes/{anime.id}/")
    anime.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Anime.objects.filter(id=anime.id).exists()
    assert not anime.is_available


@pytest.mark.django_db
def test_list_characters_by_anime(anonymous_user, anime, character):
    CharacterAnimeFactory(character_id=character, anime_id=anime)
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/characters/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 1


@pytest.mark.django_db
def test_list_characters_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/characters/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No characters found for this anime."


@pytest.mark.django_db
def test_list_staff_by_anime(anonymous_user, anime):
    staff_one = PersonFactory()
    staff_two = PersonFactory()
    StaffAnimeFactory(person_id=staff_one, anime_id=anime)
    StaffAnimeFactory(person_id=staff_two, anime_id=anime)
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/staff/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
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
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No staff found for this anime."


@pytest.mark.django_db
def test_retrieve_stats_by_anime(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/stats/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert "id" in response.data
    assert "watching" in response.data
    assert "completed" in response.data
    assert "on_hold" in response.data
    assert "dropped" in response.data
    assert "plan_to_watch" in response.data
    assert "total" in response.data


@pytest.mark.django_db
def test_retrieve_stats_by_anime_errors(anonymous_user):
    anime_id = "88bf5d4f-115b-4dea-a7c5-4fc45b794c9a"
    response = anonymous_user.get(f"/api/v1/animes/{anime_id}/stats/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "Not found."


@pytest.mark.django_db
def test_list_reviews_by_anime(anonymous_user, anime):
    review = ReviewFactory(
        content_type=ContentType.objects.get_for_model(Anime),
        object_id=anime.id,
    )
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/reviews/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0
    assert str(response.data[0]["id"]) == str(review.id)


@pytest.mark.django_db
def test_create_review_by_anime(member_user, anime, review):
    data = {
        "comment": "Review created",
        "is_spoiler": review.is_spoiler,
        "rating": review.rating,
    }
    response = member_user.post(
        f"/api/v1/animes/{anime.id}/reviews/create/", data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
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
    assert response.reason_phrase == "OK"
    anime.refresh_from_db()
    assert response.data["comment"] == "Review updated"


@pytest.mark.django_db
def test_list_recommendations_by_anime(anonymous_user, theme, genre):
    anime = AnimeFactory(genres=[genre], themes=[theme])
    AnimeFactory.create_batch(3, genres=[genre], themes=[theme])
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/recommendations/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_recommendations_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/recommendations/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No recommendations found for this anime."


@pytest.mark.django_db
def test_list_news_by_anime(anonymous_user, anime):
    NewsFactory.create_batch(3, anime_relations=[anime])
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/news/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_news_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/news/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No news found for this anime."


@pytest.mark.django_db
def test_list_videos_by_anime(anonymous_user, anime):
    VideoFactory.create_batch(
        3,
        content_type=ContentType.objects.get_for_model(Anime),
        object_id=anime.id,
    )
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/videos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_videos_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/videos/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No videos found for this anime."


@pytest.mark.django_db
def test_list_pictures_by_anime(anonymous_user, anime):
    PictureFactory.create_batch(
        3,
        content_type=ContentType.objects.get_for_model(Anime),
        object_id=anime.id,
    )
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/pictures/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_pictures_by_anime_errors(anonymous_user, anime):
    response = anonymous_user.get(f"/api/v1/animes/{anime.id}/pictures/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No pictures found for this anime."
