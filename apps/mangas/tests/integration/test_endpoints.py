"""Endpoint Tests for Mangas App."""

import pytest
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APIClient

from apps.characters.tests.factories import CharacterMangaFactory
from apps.news.tests.factories import NewsFactory
from apps.persons.choices import CategoryChoices
from apps.persons.tests.factories import PersonFactory
from apps.reviews.models import Review
from apps.reviews.tests.factories import ReviewFactory
from apps.users.tests.factories import MemberFactory
from apps.utils.tests.factories import PictureFactory
from ...models import Magazine, Manga
from ..factories import MangaFactory


@pytest.mark.django_db
def test_list_magazines(anonymous_user, magazine):
    response = anonymous_user.get("/api/v1/magazines/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_magazine(anonymous_user, magazine):
    response = anonymous_user.get(f"/api/v1/magazines/{magazine.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert str(response.data["id"]) == str(magazine.id)
    assert response.data["name"] == magazine.name


@pytest.mark.django_db
def test_retrieve_magazine_errors(anonymous_user):
    response = anonymous_user.get(
        "/api/v1/magazines/124f0ff1-5236-4cdb-9f0f-c0057e8d805f/"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_magazine(contributor_user):
    data = {"name": "New Magazine"}
    response = contributor_user.post("/api/v1/magazines/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Magazine.objects.filter(name="New Magazine").exists()
    assert response.data["name"] == "New Magazine"


@pytest.mark.django_db
def test_create_magazine_unauthorized(member_user):
    data = {"name": "Unauthorized Magazine"}
    member_response = member_user.post("/api/v1/magazines/", data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    member_user.logout()
    anonymus_response = member_user.post("/api/v1/magazines/", data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert not Magazine.objects.filter(name="Unauthorized Magazine").exists()


@pytest.mark.django_db
def test_update_magazine(contributor_user, magazine):
    data = {"name": "Updated Magazine"}
    response = contributor_user.put(
        f"/api/v1/magazines/{magazine.id}/", data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    magazine.refresh_from_db()
    assert magazine.name == "Updated Magazine"


@pytest.mark.django_db
def test_partial_update_magazine(contributor_user, magazine):
    data = {"name": "Partially Updated Magazine"}
    response = contributor_user.patch(
        f"/api/v1/magazines/{magazine.id}/",
        data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    magazine.refresh_from_db()
    assert magazine.name == "Partially Updated Magazine"


@pytest.mark.django_db
def test_delete_magazine(contributor_user, magazine):
    assert magazine.is_available
    response = contributor_user.delete(f"/api/v1/magazines/{magazine.id}/")
    magazine.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Magazine.objects.filter(id=magazine.id).exists()
    assert not magazine.is_available


@pytest.mark.django_db
def test_list_mangas(anonymous_user, manga):
    response = anonymous_user.get("/api/v1/mangas/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_manga(anonymous_user, manga):
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(manga.id)
    assert response.data["name"] == manga.name


@pytest.mark.django_db
def test_retrieve_manga_not_found(anonymous_user):
    response = anonymous_user.get(
        "/api/v1/magazines/124f0ff1-5236-4cdb-9f0f-c0057e8d805f/"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_create_manga(contributor_user, manga, demographic):
    author = PersonFactory.create(category=CategoryChoices.ARTIST)
    data = {
        "name": "Oyasumi Punpun",
        "name_jpn": "おやすみプンプン",
        "image": manga.image,
        "synopsis": manga.synopsis,
        "background": manga.background,
        "media_type": manga.media_type,
        "volumes": manga.volumes,
        "chapters": manga.chapters,
        "status": manga.status,
        "published_from": manga.published_from,
        "published_to": manga.published_to,
        "genres": [str(genre.id) for genre in manga.genres.all()],
        "themes": [str(theme.id) for theme in manga.themes.all()],
        "demographic_id": str(manga.demographic_id.id),
        "serialization_id": str(manga.serialization_id.id),
        "author_id": str(author.id),
        "website": manga.website,
    }
    response = contributor_user.post(
        "/api/v1/mangas/",
        data,
        format="multipart",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Manga.objects.filter(name="Oyasumi Punpun").exists()
    assert response.data["name"] == "Oyasumi Punpun"
    assert response.data["name_jpn"] == "おやすみプンプン"


@pytest.mark.django_db
def test_create_manga_unauthorized(member_user):
    data = {}
    member_response = member_user.post("/api/v1/mangas/", data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post("/api/v1/mangas/", data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"
    assert not Manga.objects.filter(name="Unauthorized manga").exists()


@pytest.mark.django_db
def test_update_manga(contributor_user, manga):
    author = PersonFactory.create(category=CategoryChoices.ARTIST)
    data = {
        "name": "Frieren: Beyond Journey's End",
        "name_jpn": "葬送のフリーレン",
        "image": manga.image,
        "synopsis": manga.synopsis,
        "background": manga.background,
        "media_type": manga.media_type,
        "volumes": manga.volumes,
        "chapters": manga.chapters,
        "status": manga.status,
        "published_from": manga.published_from,
        "published_to": manga.published_to,
        "genres": [str(genre.id) for genre in manga.genres.all()],
        "themes": [str(theme.id) for theme in manga.themes.all()],
        "demographic_id": str(manga.demographic_id.id),
        "serialization_id": str(manga.serialization_id.id),
        "author_id": str(author.id),
        "website": manga.website,
    }
    response = contributor_user.put(
        f"/api/v1/mangas/{manga.id}/", data, format="multipart"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    manga.refresh_from_db()
    assert manga.name == "Frieren: Beyond Journey's End"
    assert manga.name_jpn == "葬送のフリーレン"


@pytest.mark.django_db
def test_partial_update_manga(contributor_user, manga):
    data = {"name": "Houseki no Kuni"}
    response = contributor_user.patch(
        f"/api/v1/mangas/{manga.id}/", data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    manga.refresh_from_db()
    assert manga.name == "Houseki no Kuni"


@pytest.mark.django_db
def test_delete_manga(contributor_user, manga):
    assert manga.is_available
    response = contributor_user.delete(f"/api/v1/mangas/{manga.id}/")
    manga.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Manga.objects.filter(id=manga.id).exists()
    assert not manga.is_available


@pytest.mark.django_db
def test_list_characters_by_manga(anonymous_user, character, manga):
    CharacterMangaFactory(character_id=character, manga_id=manga)
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/characters/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 1


@pytest.mark.django_db
def test_list_characters_by_manga_errors(anonymous_user, manga):
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/characters/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No characters found for this manga."


@pytest.mark.django_db
def test_retrieve_stats_by_manga(anonymous_user, manga):
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/stats/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert "id" in response.data
    assert "reading" in response.data
    assert "completed" in response.data
    assert "on_hold" in response.data
    assert "dropped" in response.data
    assert "plan_to_read" in response.data
    assert "total" in response.data


@pytest.mark.django_db
def test_retrieve_stats_by_manga_errors(anonymous_user):
    manga_id = "88bf5d4f-115b-4dea-a7c5-4fc45b794c9a"
    response = anonymous_user.get(f"/api/v1/mangas/{manga_id}/stats/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "Not found."


@pytest.mark.django_db
def test_list_reviews_by_manga(anonymous_user, manga):
    review = ReviewFactory(
        content_type=ContentType.objects.get_for_model(Manga),
        object_id=manga.id,
    )
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/reviews/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0
    assert str(response.data[0]["id"]) == str(review.id)


@pytest.mark.django_db
def test_create_review_by_manga(member_user, manga, review):
    data = {
        "comment": "Review created",
        "is_spoiler": review.is_spoiler,
        "rating": review.rating,
    }
    response = member_user.post(
        f"/api/v1/mangas/{manga.id}/reviews/create/", data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Review.objects.filter(comment="Review created").exists()
    assert response.data["comment"] == "Review created"


@pytest.mark.django_db
def test_update_review_by_manga(manga):
    user = MemberFactory()
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    review = ReviewFactory(
        user_id=user,
        content_type=ContentType.objects.get_for_model(Manga),
        object_id=manga.id,
    )
    data = {
        "comment": "Review updated",
        "is_spoiler": review.is_spoiler,
        "rating": review.rating,
    }
    response = api_client.patch(
        f"/api/v1/mangas/{manga.id}/reviews/{review.id}/", data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    manga.refresh_from_db()
    assert response.data["comment"] == "Review updated"


@pytest.mark.django_db
def test_list_recommendations_by_manga(anonymous_user, theme, genre):
    manga = MangaFactory(genres=[genre], themes=[theme])
    MangaFactory.create_batch(3, genres=[genre], themes=[theme])
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/recommendations/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_recommendations_by_manga_errors(anonymous_user, manga):
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/recommendations/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No recommendations found for this manga."


@pytest.mark.django_db
def test_list_news_by_manga(anonymous_user, manga):
    NewsFactory.create_batch(3, manga_relations=[manga])
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/news/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_news_by_manga_errors(anonymous_user, manga):
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/news/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No news found for this manga."


@pytest.mark.django_db
def test_list_pictures_by_manga(anonymous_user, manga):
    PictureFactory.create_batch(
        3,
        content_type=ContentType.objects.get_for_model(Manga),
        object_id=manga.id,
    )
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/pictures/")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_pictures_by_manga_errors(anonymous_user, manga):
    response = anonymous_user.get(f"/api/v1/mangas/{manga.id}/pictures/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No pictures found for this manga."
