"""ViewSet Tests for Genres App."""

import uuid
import pytest
from rest_framework import status

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from .factories import GenreFactory, ThemeFactory, DemographicFactory
from ..models import Genre, Theme, Demographic


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
class TestThemeViewSet:

    def test_list_themes(self, anonymous_user, theme):
        response = anonymous_user.get("/api/v1/themes/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0

    def test_retrieve_theme(self, anonymous_user, theme):
        response = anonymous_user.get(f"/api/v1/themes/{theme.id}/")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert uuid.UUID(data["id"]) == theme.id
        assert data["name"] == theme.name

    def test_retrieve_theme_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/themes/989423d1-d6c0-431a-8f62-d805b8a5f321/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_theme(self, contributor_user):
        data = {"name": "New Theme"}
        response = contributor_user.post("/api/v1/themes/", data, format="json")

        data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert Theme.objects.filter(name="New Theme").exists()
        assert data["name"] == "New Theme"

    def test_create_theme_unauthorized(self, member_user):
        data = {"name": "Unauthorized Theme"}
        member_response = member_user.post("/api/v1/themes/", data, format="json")
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post("/api/v1/themes/", data, format="json")
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Theme.objects.filter(name="Unauthorized Theme").exists()

    def test_update_theme(self, contributor_user, theme):
        data = {"name": "Updated Theme"}
        response = contributor_user.put(
            f"/api/v1/themes/{theme.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        theme.refresh_from_db()
        assert theme.name == "Updated Theme"

    def test_partial_update_theme(self, contributor_user, theme):
        data = {"name": "Partially Updated Theme"}
        response = contributor_user.patch(
            f"/api/v1/themes/{theme.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        theme.refresh_from_db()
        assert theme.name == "Partially Updated Theme"

    def test_delete_theme(self, contributor_user, theme):
        assert theme.is_available

        response = contributor_user.delete(f"/api/v1/themes/{theme.id}/")
        theme.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Theme.objects.filter(id=theme.id).exists()
        assert not theme.is_available

    def test_search_field_name(self, member_user):
        ThemeFactory(name="Harem")
        ThemeFactory(name="Gore")
        ThemeFactory(name="Isekai")

        response = member_user.get("/api/v1/themes/", {"q": "Harem"})
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert len(data["results"]) == 1
        assert data["results"][0]["name"] == "Harem"

        response_partial = member_user.get("/api/v1/themes/", {"q": "Gore"})
        data_partial = response_partial.json()
        assert response_partial.status_code == status.HTTP_200_OK
        assert len(data_partial["results"]) == 1
        assert data_partial["results"][0]["name"] == "Gore"

        response_no_results = member_user.get(
            "/api/v1/themes/", {"q": "Music"}  # Not Found
        )
        data_no_results = response_no_results.json()
        assert response_no_results.status_code == status.HTTP_200_OK
        assert len(data_no_results["results"]) == 0


@pytest.mark.django_db
class TestDemographicViewSet:

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

    def test_retrieve_demographic_not_found(self, anonymous_user):
        response = anonymous_user.get(
            "/api/v1/demographics/989423d1-d6c0-431a-8f62-d805b8a5f321/"
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_create_demographic(self, contributor_user):
        data = {"name": "New Demographic"}
        response = contributor_user.post("/api/v1/demographics/", data, format="json")

        data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert Demographic.objects.filter(name="New Demographic").exists()
        assert data["name"] == "New Demographic"

    def test_create_demographic_unauthorized(self, member_user):
        data = {"name": "Unauthorized Demographic"}
        member_response = member_user.post("/api/v1/demographics/", data, format="json")
        assert member_response.status_code == status.HTTP_403_FORBIDDEN

        member_user.logout()

        anonymus_response = member_user.post(
            "/api/v1/demographics/", data, format="json"
        )
        assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED

        assert not Demographic.objects.filter(name="Unauthorized Demographic").exists()

    def test_update_demographic(self, contributor_user, demographic):
        data = {"name": "Updated Demographic"}
        response = contributor_user.put(
            f"/api/v1/demographics/{demographic.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        demographic.refresh_from_db()
        assert demographic.name == "Updated Demographic"

    def test_partial_update_demographic(self, contributor_user, demographic):
        data = {"name": "Partially Updated Demographic"}
        response = contributor_user.patch(
            f"/api/v1/demographics/{demographic.id}/",
            data,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        demographic.refresh_from_db()
        assert demographic.name == "Partially Updated Demographic"

    def test_delete_demographic(self, contributor_user, demographic):
        assert demographic.is_available

        response = contributor_user.delete(f"/api/v1/demographics/{demographic.id}/")
        demographic.refresh_from_db()

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Demographic.objects.filter(id=demographic.id).exists()
        assert not demographic.is_available

    def test_search_field_name(self, member_user):
        DemographicFactory(name="Harem")
        DemographicFactory(name="Gore")
        DemographicFactory(name="Isekai")

        response = member_user.get("/api/v1/demographics/", {"q": "Harem"})
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert len(data["results"]) == 1
        assert data["results"][0]["name"] == "Harem"

        response_partial = member_user.get("/api/v1/demographics/", {"q": "Gore"})
        data_partial = response_partial.json()
        assert response_partial.status_code == status.HTTP_200_OK
        assert len(data_partial["results"]) == 1
        assert data_partial["results"][0]["name"] == "Gore"

        response_no_results = member_user.get(
            "/api/v1/demographics/", {"q": "Music"}  # Not Found
        )
        data_no_results = response_no_results.json()
        assert response_no_results.status_code == status.HTTP_200_OK
        assert len(data_no_results["results"]) == 0
