"""Endpoint Tests for Randoms App."""

import pytest


@pytest.mark.django_db
def test_random_list(anonymous_user, anime):
    response = anonymous_user.get("/api/v1/random/anime/")

    assert response.status_code == 200
    assert len(response.json()) > 0
