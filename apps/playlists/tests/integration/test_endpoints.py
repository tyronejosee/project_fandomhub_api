"""Endpoint Tests for Playlists App."""

import pytest
from rest_framework import status

from ...models import AnimeListItem
from ...choices import AnimeStatusChoices
from ..factories import AnimeListFactory, AnimeListItemFactory


@pytest.mark.django_db
def test_retrieve_animelist(member_user):
    endpoint = "/api/v1/playlists/animelist/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert "id" in response.data
    assert "banner" in response.data
    assert "is_public" in response.data
    assert "created_at" in response.data
    assert "updated_at" in response.data


@pytest.mark.django_db
def test_retrieve_animelist_errors(anonymous_user):
    endpoint = "/api/v1/playlists/animelist/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.reason_phrase == "Unauthorized"
    assert response.data["detail"] == "Authentication credentials were not provided."


@pytest.mark.django_db
def test_partial_update_animelist(member_user):
    endpoint = "/api/v1/playlists/animelist/"
    data = {"is_public": False}
    response = member_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert not response.data["is_public"]


@pytest.mark.django_db
def test_partial_update_animelist_errors(member_user):
    endpoint = "/api/v1/playlists/animelist/"
    data = {"is_public": "String field"}
    response = member_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.reason_phrase == "Bad Request"
    assert response.data["is_public"][0] == "Must be a valid boolean."


@pytest.mark.django_db
def test_list_animelist_item(member_user):
    endpoint = "/api/v1/playlists/animelist/animes/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert response.data["detail"] == "Your animelist is empty."


@pytest.mark.django_db
def test_create_animelist_item(member_user, anime_list_item, anime):
    endpoint = "/api/v1/playlists/animelist/animes/"
    data = {
        "anime_id": anime.id,
        "status": anime_list_item.status,
        "episodes_watched": anime_list_item.episodes_watched,
        "score": anime_list_item.score,
        "start_date": anime_list_item.start_date,
        "finish_date": anime_list_item.finish_date,
        "priority": anime_list_item.priority,
        "storage": anime_list_item.storage,
        "times_rewatched": anime_list_item.times_rewatched,
        "notes": anime_list_item.notes,
        "order": anime_list_item.order,
        "is_watched": anime_list_item.is_watched,
        "is_favorite": anime_list_item.is_favorite,
    }
    response = member_user.post(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert str(response.data["anime_id"]) == str(anime.id)
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"


@pytest.mark.django_db
def test_retrieve_animelist_item(api_client_with_member_user):
    api_client, user = api_client_with_member_user
    animelist = AnimeListFactory.create(user=user)
    item = AnimeListItemFactory.create(animelist_id=animelist)
    endpoint = f"/api/v1/playlists/animelist/animes/{item.id}/"
    response = api_client.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert "id" in response.data
    assert "anime_id" in response.data
    assert "status" in response.data
    assert "episodes_watched" in response.data
    assert "score" in response.data
    assert "start_date" in response.data
    assert "finish_date" in response.data
    assert "tags" in response.data
    assert "priority" in response.data
    assert "storage" in response.data
    assert "times_rewatched" in response.data
    assert "notes" in response.data
    assert "order" in response.data
    assert "is_watched" in response.data
    assert "is_favorite" in response.data
    assert "created_at" in response.data
    assert "updated_at" in response.data


@pytest.mark.django_db
def test_partial_update_animelist_item(api_client_with_member_user):
    api_client, user = api_client_with_member_user
    animelist = AnimeListFactory.create(user=user)
    item = AnimeListItemFactory.create(animelist_id=animelist)
    endpoint = f"/api/v1/playlists/animelist/animes/{item.id}/"
    data = {"status": "watching"}
    response = api_client.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert response.data["status"] == AnimeStatusChoices.WATCHING


@pytest.mark.django_db
def test_delete_animelist_item(api_client_with_member_user):
    api_client, user = api_client_with_member_user
    animelist = AnimeListFactory.create(user=user)
    item = AnimeListItemFactory.create(animelist_id=animelist)
    endpoint = f"/api/v1/playlists/animelist/animes/{item.id}/"
    response = api_client.delete(endpoint)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert AnimeListItem.objects.filter(id=item.id).exists()
