"""Endpoint Tests for Producers App."""

# import uuid
import pytest


@pytest.mark.django_db
class TestGenreEndpoints:

    def test_list_producers(self, anonymous_user, producer):
        response = anonymous_user.get("/api/v1/producers/")

        assert response.status_code == 200
        assert len(response.json()) > 0
