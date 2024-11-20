"""ViewSet Tests for Genres App."""

import uuid
import pytest
from rest_framework import status

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from apps.genres.tests.factories import GenreFactory
from ..models import Genre


@pytest.mark.django_db
class TestGenreViewSet:

    def test_list_genres(self, anonymous_user, genre):
        response = anonymous_user.get("/api/v1/genres/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0

    def test_retrieve_genre(self, anonymous_user, genre):
        response = anonymous_user.get(f"/api/v1/genres/{genre.id}/")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(data["id"]) == genre.id
        assert data["name"] == genre.name

    def test_retrieve_genre_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/genres/989423d1-d6c0-431a-8f62-d805b8a5f321/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_genre(self, contributor_user):
        data = {"name": "New Genre"}
        response = contributor_user.post("/api/v1/genres/", data, format="json")

        data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert Genre.objects.filter(name="New Genre").exists()
        assert data["name"] == "New Genre"

    def test_create_genre_unauthorized(self, member_user):
        data = {"name": "Unauthorized Genre"}
        member_response = member_user.post("/api/v1/genres/", data, format="json")
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post("/api/v1/genres/", data, format="json")
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Genre.objects.filter(name="Unauthorized Genre").exists()

    def test_update_genre(self, contributor_user, genre):
        data = {"name": "Updated Genre"}
        response = contributor_user.put(
            f"/api/v1/genres/{genre.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        genre.refresh_from_db()
        assert genre.name == "Updated Genre"

    def test_partial_update_genre(self, contributor_user, genre):
        data = {"name": "Partially Updated Genre"}
        response = contributor_user.patch(
            f"/api/v1/genres/{genre.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        genre.refresh_from_db()
        assert genre.name == "Partially Updated Genre"

    def test_delete_genre(self, contributor_user, genre):
        assert genre.is_available

        response = contributor_user.delete(f"/api/v1/genres/{genre.id}/")
        genre.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Genre.objects.filter(id=genre.id).exists()
        assert not genre.is_available

    def test_search_field_name(self, member_user):
        GenreFactory(name="Action")
        GenreFactory(name="Comedy")
        GenreFactory(name="Supernatural")

        response = member_user.get("/api/v1/genres/", {"q": "Action"})
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert len(data["results"]) == 1
        assert data["results"][0]["name"] == "Action"

        response_partial = member_user.get("/api/v1/genres/", {"q": "Comedy"})
        data_partial = response_partial.json()
        assert response_partial.status_code == status.HTTP_200_OK
        assert len(data_partial["results"]) == 1
        assert data_partial["results"][0]["name"] == "Comedy"

        response_no_results = member_user.get(
            "/api/v1/genres/", {"q": "Slice of Life"}  # Not Found
        )
        data_no_results = response_no_results.json()
        assert response_no_results.status_code == status.HTTP_200_OK
        assert len(data_no_results["results"]) == 0

    def test_get_animes_with_results(self, member_user):
        genre = GenreFactory()
        AnimeFactory.create_batch(3, genres=[genre])
        response = member_user.get(f"/api/v1/genres/{genre.id}/animes/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_get_animes_no_results(self, member_user):
        genre = GenreFactory()
        response = member_user.get(f"/api/v1/genres/{genre.id}/animes/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No animes found for this genre."

    def test_get_mangas_with_results(self, member_user):
        genre = GenreFactory()
        MangaFactory.create_batch(3, genres=[genre])
        response = member_user.get(f"/api/v1/genres/{genre.id}/mangas/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 3

    def test_get_mangas_no_results(self, member_user):
        genre = GenreFactory()
        response = member_user.get(f"/api/v1/genres/{genre.id}/mangas/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "No mangas found for this genre."


@pytest.mark.django_db
class TestThemeEndpoints:

    def test_list_genres(self, anonymous_user, theme):
        response = anonymous_user.get("/api/v1/themes/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0

    def test_retrieve_theme(self, anonymous_user, theme):
        response = anonymous_user.get(f"/api/v1/themes/{theme.id}/")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(data["id"]) == theme.id
        assert data["name"] == theme.name


@pytest.mark.django_db
class TestDemographicEndpoints:

    def test_list_demographics(self, anonymous_user, demographic):
        response = anonymous_user.get("/api/v1/demographics/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0

    def test_retrieve_demographic(self, anonymous_user, demographic):
        response = anonymous_user.get(f"/api/v1/demographics/{demographic.id}/")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(data["id"]) == demographic.id
        assert data["name"] == demographic.name
