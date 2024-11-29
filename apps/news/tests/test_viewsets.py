"""ViewSet Tests for News App."""

import pytest
from rest_framework import status

from apps.utils.functions import generate_test_image
from ..models import News


@pytest.mark.django_db
class TestNewsViewSet:
    """Tests for AnimeViewSet"""

    def test_list_news(self, anonymous_user, news):
        response = anonymous_user.get("/api/v1/news/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) > 0

    def test_retrieve_news(self, anonymous_user, news):
        response = anonymous_user.get(f"/api/v1/news/{news.id}/")
        assert response.status_code == status.HTTP_200_OK
        assert str(response.data["id"]) == str(news.id)
        assert response.data["name"] == news.name

    def test_create_news(self, moderator_user, news):
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "Lorem ipsum",
            "description": news.description,
            "content": news.content,
            "image": image,
            "source": news.source,
            "tag": news.tag,
            "author_id": str(news.author_id.id),
        }
        response = moderator_user.post(
            "/api/v1/news/",
            data,
            format="multipart",
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert News.objects.filter(name="Lorem ipsum").exists()
        assert response.data["name"] == "Lorem ipsum"

    def test_create_news_unauthorized(self, member_user):
        data = {}
        member_response = member_user.post("/api/v1/news/", data, format="json")
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post("/api/v1/news/", data, format="json")
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_news(self, moderator_user, news):
        image = generate_test_image(size=(600, 600))
        data = {
            "name": "Updated News",
            "description": news.description,
            "content": news.content,
            "image": image,
            "source": news.source,
            "tag": news.tag,
            "author_id": str(news.author_id.id),
        }
        response = moderator_user.put(
            f"/api/v1/news/{news.id}/", data, format="multipart"
        )
        assert response.status_code == status.HTTP_200_OK
        news.refresh_from_db()
        assert news.name == "Updated News"

    def test_partial_update_news(self, moderator_user, news):
        data = {"name": "Partially Updated News"}
        response = moderator_user.patch(f"/api/v1/news/{news.id}/", data, format="json")
        assert response.status_code == status.HTTP_200_OK
        news.refresh_from_db()
        assert news.name == "Partially Updated News"

    def test_delete_news(self, moderator_user, news):
        assert news.is_available
        response = moderator_user.delete(f"/api/v1/news/{news.id}/")
        news.refresh_from_db()
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert News.objects.filter(id=news.id).exists()
        assert not news.is_available
