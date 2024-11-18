"""Endpoint Tests for Genres App."""

import uuid
import pytest

from ..models import Genre


@pytest.mark.django_db
class TestGenreEndpoints:

    def test_list_genres(self, anonymous_user, genre):
        response = anonymous_user.get("/api/v1/genres/")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_retrieve_genre(self, anonymous_user, genre):
        response = anonymous_user.get(f"/api/v1/genres/{genre.id}/")
        data = response.json()

        assert response.status_code == 200
        assert uuid.UUID(data["id"]) == genre.id
        assert data["name"] == genre.name

    def test_create_genre(self, contributor_user):
        data = {"name": "New Genre"}
        response = contributor_user.post("/api/v1/genres/", data, format="json")

        data = response.json()

        assert response.status_code == 201
        assert Genre.objects.filter(name="New Genre").exists()
        assert data["name"] == "New Genre"

    def test_create_genre_unauthorized(self, member_user):
        data = {"name": "Unauthorized Genre"}
        member_response = member_user.post("/api/v1/genres/", data, format="json")
        assert member_response.status_code == 403

        member_user.logout()

        anonymus_response = member_user.post("/api/v1/genres/", data, format="json")
        assert anonymus_response.status_code == 401

        assert not Genre.objects.filter(name="Unauthorized Genre").exists()

    def test_update_genre(self, contributor_user, genre):
        data = {"name": "Updated Genre"}
        response = contributor_user.put(
            f"/api/v1/genres/{genre.id}/",
            data,
            format="json",
        )

        assert response.status_code == 200
        genre.refresh_from_db()
        assert genre.name == "Updated Genre"

    def test_partial_update_genre(self, contributor_user, genre):
        data = {"name": "Partially Updated Genre"}
        response = contributor_user.put(
            f"/api/v1/genres/{genre.id}/",
            data,
            format="json",
        )

        assert response.status_code == 200
        genre.refresh_from_db()
        assert genre.name == "Partially Updated Genre"

    def test_delete_genre(self, contributor_user, genre):
        assert genre.is_available

        response = contributor_user.delete(f"/api/v1/genres/{genre.id}/")
        genre.refresh_from_db()

        assert response.status_code == 204
        assert Genre.objects.filter(id=genre.id).exists()
        assert not genre.is_available


@pytest.mark.django_db
class TestThemeEndpoints:

    def test_list_genres(self, anonymous_user, theme):
        response = anonymous_user.get("/api/v1/themes/")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_retrieve_theme(self, anonymous_user, theme):
        response = anonymous_user.get(f"/api/v1/themes/{theme.id}/")
        data = response.json()

        assert response.status_code == 200
        assert uuid.UUID(data["id"]) == theme.id
        assert data["name"] == theme.name


@pytest.mark.django_db
class TestDemographicEndpoints:

    def test_list_demographics(self, anonymous_user, demographic):
        response = anonymous_user.get("/api/v1/demographics/")

        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_retrieve_demographic(self, anonymous_user, demographic):
        response = anonymous_user.get(f"/api/v1/demographics/{demographic.id}/")
        data = response.json()

        assert response.status_code == 200
        assert uuid.UUID(data["id"]) == demographic.id
        assert data["name"] == demographic.name
