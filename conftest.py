import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from apps.genres.tests.factories import GenreFactory

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(
        email="testuser@example.com",
        username="testuser",
        password="password123",
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_token(client, user):
    url = "api/v1/auth/token/login/"
    response = client.post(url, {"username": "testuser", "password": "password123"})

    assert response.status_code == 200
    return response.data["auth_token"]


@pytest.fixture
def genre():
    return GenreFactory.create()
