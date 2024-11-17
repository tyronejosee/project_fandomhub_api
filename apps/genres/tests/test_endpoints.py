"""Endpoint Tests for Genres App."""

import uuid
import pytest


@pytest.mark.django_db
def test_genre_list(api_client, genre):
    response = api_client.get("/api/v1/genres/")

    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_genre_detail(api_client, genre):
    response = api_client.get(f"/api/v1/genres/{genre.id}/")
    data = response.json()

    assert response.status_code == 200
    assert uuid.UUID(data["id"]) == genre.id
    assert data["name"] == genre.name


@pytest.mark.django_db
def test_theme_list(api_client, theme):
    response = api_client.get("/api/v1/themes/")

    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_theme_detail(api_client, theme):
    response = api_client.get(f"/api/v1/themes/{theme.id}/")
    data = response.json()

    assert response.status_code == 200
    assert uuid.UUID(data["id"]) == theme.id
    assert data["name"] == theme.name


@pytest.mark.django_db
def test_demographic_list(api_client, demographic):
    response = api_client.get("/api/v1/demographics/")

    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.django_db
def test_demographic_detail(api_client, demographic):
    response = api_client.get(f"/api/v1/demographics/{demographic.id}/")
    data = response.json()

    assert response.status_code == 200
    assert uuid.UUID(data["id"]) == demographic.id
    assert data["name"] == demographic.name
