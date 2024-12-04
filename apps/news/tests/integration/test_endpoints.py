"""Endpoint Tests for News App."""

import pytest
from rest_framework import status

from apps.utils.functions import generate_test_image
from ...models import News


@pytest.mark.django_db
def test_list_news(anonymous_user, news):
    endpoint = "/api/v1/news/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_news(anonymous_user, news):
    endpoint = f"/api/v1/news/{news.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(news.id)
    assert response.data["name"] == news.name


@pytest.mark.django_db
def test_create_news(moderator_user, news):
    image = generate_test_image(size=(600, 600))
    endpoint = "/api/v1/news/"
    data = {
        "name": "Lorem ipsum",
        "description": news.description,
        "content": news.content,
        "image": image,
        "source": news.source,
        "tag": news.tag,
        "author_id": str(news.author_id.id),
    }
    response = moderator_user.post(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert News.objects.filter(name="Lorem ipsum").exists()
    assert response.data["name"] == "Lorem ipsum"


@pytest.mark.django_db
def test_create_news_errors(member_user):
    endpoint = "/api/v1/news/"
    data = {}
    member_response = member_user.post(endpoint, data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post(endpoint, data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"


@pytest.mark.django_db
def test_update_news(moderator_user, news):
    image = generate_test_image(size=(600, 600))
    endpoint = f"/api/v1/news/{news.id}/"
    data = {
        "name": "Updated News",
        "description": news.description,
        "content": news.content,
        "image": image,
        "source": news.source,
        "tag": news.tag,
        "author_id": str(news.author_id.id),
    }
    response = moderator_user.put(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    news.refresh_from_db()
    assert news.name == "Updated News"


@pytest.mark.django_db
def test_partial_update_news(moderator_user, news):
    endpoint = f"/api/v1/news/{news.id}/"
    data = {"name": "Partially Updated News"}
    response = moderator_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    news.refresh_from_db()
    assert news.name == "Partially Updated News"


@pytest.mark.django_db
def test_delete_news(moderator_user, news):
    assert news.is_available
    endpoint = f"/api/v1/news/{news.id}/"
    response = moderator_user.delete(endpoint)
    news.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert News.objects.filter(id=news.id).exists()
    assert not news.is_available
