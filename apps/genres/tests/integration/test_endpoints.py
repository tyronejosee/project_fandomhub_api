"""Endpoints Tests for Genres App."""

import pytest
from rest_framework import status

from apps.animes.tests.factories import AnimeFactory
from apps.mangas.tests.factories import MangaFactory
from ..factories import GenreFactory, ThemeFactory, DemographicFactory
from ...models import Genre, Theme, Demographic


@pytest.mark.django_db
def test_list_genres(anonymous_user, genre):
    endpoint = "/api/v1/genres/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_genre(anonymous_user, genre):
    endpoint = f"/api/v1/genres/{genre.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(genre.id)
    assert response.data["name"] == genre.name


@pytest.mark.django_db
def test_retrieve_genre_errors(anonymous_user):
    endpoint = "/api/v1/genres/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"


@pytest.mark.django_db
def test_create_genre(contributor_user):
    endpoint = "/api/v1/genres/"
    data = {"name": "New Genre"}
    response = contributor_user.post(endpoint, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Genre.objects.filter(name="New Genre").exists()
    assert response.data["name"] == "New Genre"


@pytest.mark.django_db
def test_create_genre_unauthorized(member_user):
    endpoint = "/api/v1/genres/"
    data = {"name": "Unauthorized Genre"}
    member_response = member_user.post(endpoint, data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post(endpoint, data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"
    assert not Genre.objects.filter(name="Unauthorized Genre").exists()


@pytest.mark.django_db
def test_update_genre(contributor_user, genre):
    endpoint = f"/api/v1/genres/{genre.id}/"
    data = {"name": "Updated Genre"}
    response = contributor_user.put(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    genre.refresh_from_db()
    assert genre.name == "Updated Genre"


@pytest.mark.django_db
def test_partial_update_genre(contributor_user, genre):
    endpoint = f"/api/v1/genres/{genre.id}/"
    data = {"name": "Partially Updated Genre"}
    response = contributor_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    genre.refresh_from_db()
    assert genre.name == "Partially Updated Genre"


@pytest.mark.django_db
def test_delete_genre(contributor_user, genre):
    assert genre.is_available
    endpoint = f"/api/v1/genres/{genre.id}/"
    response = contributor_user.delete(endpoint)
    genre.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Genre.objects.filter(id=genre.id).exists()
    assert not genre.is_available


@pytest.mark.django_db
def test_search_genre_field_name(member_user):
    GenreFactory(name="Action")
    GenreFactory(name="Comedy")
    GenreFactory(name="Supernatural")
    endpoint = "/api/v1/genres/"

    response = member_user.get(endpoint, {"q": "Action"})
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Action"

    response_partial = member_user.get(endpoint, {"q": "Comedy"})
    assert response_partial.status_code == status.HTTP_200_OK
    assert response_partial.reason_phrase == "OK"
    assert len(response_partial.data["results"]) == 1
    assert response_partial.data["results"][0]["name"] == "Comedy"

    response_no_results = member_user.get(endpoint, {"q": "Slice of Life"})  # Not Found
    assert response_no_results.status_code == status.HTTP_200_OK
    assert response_no_results.reason_phrase == "OK"
    assert len(response_no_results.data["results"]) == 0


@pytest.mark.django_db
def test_get_animes_by_genre(member_user):
    genre = GenreFactory()
    AnimeFactory.create_batch(3, genres=[genre])
    endpoint = f"/api/v1/genres/{genre.id}/animes/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_get_animes_by_genre_errors(member_user):
    genre = GenreFactory()
    endpoint = f"/api/v1/genres/{genre.id}/animes/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No animes found for this genre."


@pytest.mark.django_db
def test_get_mangas_with_results(member_user):
    genre = GenreFactory()
    MangaFactory.create_batch(3, genres=[genre])
    endpoint = f"/api/v1/genres/{genre.id}/mangas/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_get_mangas_errors(member_user):
    genre = GenreFactory()
    endpoint = f"/api/v1/genres/{genre.id}/mangas/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No mangas found for this genre."


@pytest.mark.django_db
def test_list_themes(anonymous_user, theme):
    endpoint = "/api/v1/themes/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_theme(anonymous_user, theme):
    endpoint = f"/api/v1/themes/{theme.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(theme.id)
    assert response.data["name"] == theme.name


@pytest.mark.django_db
def test_retrieve_theme_errors(anonymous_user):
    endpoint = "/api/v1/themes/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"


@pytest.mark.django_db
def test_create_theme(contributor_user):
    endpoint = "/api/v1/themes/"
    data = {"name": "New Theme"}
    response = contributor_user.post(endpoint, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Theme.objects.filter(name="New Theme").exists()
    assert response.data["name"] == "New Theme"


@pytest.mark.django_db
def test_create_theme_errors(member_user):
    endpoint = "/api/v1/themes/"
    data = {"name": "Unauthorized Theme"}
    member_response = member_user.post(endpoint, data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post(endpoint, data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"
    assert not Theme.objects.filter(name="Unauthorized Theme").exists()


@pytest.mark.django_db
def test_update_theme(contributor_user, theme):
    endpoint = f"/api/v1/themes/{theme.id}/"
    data = {"name": "Updated Theme"}
    response = contributor_user.put(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    theme.refresh_from_db()
    assert theme.name == "Updated Theme"


@pytest.mark.django_db
def test_partial_update_theme(contributor_user, theme):
    endpoint = f"/api/v1/themes/{theme.id}/"
    data = {"name": "Partially Updated Theme"}
    response = contributor_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    theme.refresh_from_db()
    assert theme.name == "Partially Updated Theme"


@pytest.mark.django_db
def test_delete_theme(contributor_user, theme):
    assert theme.is_available
    endpoint = f"/api/v1/themes/{theme.id}/"
    response = contributor_user.delete(endpoint)
    theme.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Theme.objects.filter(id=theme.id).exists()
    assert not theme.is_available


@pytest.mark.django_db
def test_search_theme(member_user):
    ThemeFactory(name="Harem")
    ThemeFactory(name="Gore")
    ThemeFactory(name="Isekai")
    endpoint = "/api/v1/themes/"

    response = member_user.get(endpoint, {"q": "Harem"})
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Harem"

    response_partial = member_user.get(endpoint, {"q": "Gore"})
    assert response_partial.status_code == status.HTTP_200_OK
    assert response_partial.reason_phrase == "OK"
    assert len(response_partial.data["results"]) == 1
    assert response_partial.data["results"][0]["name"] == "Gore"

    response_no_results = member_user.get(endpoint, {"q": "Music"})  # Not Found
    assert response_no_results.status_code == status.HTTP_200_OK
    assert response_no_results.reason_phrase == "OK"
    assert len(response_no_results.data["results"]) == 0


@pytest.mark.django_db
def test_list_demographics(anonymous_user, demographic):
    endpoint = "/api/v1/demographics/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_demographic(anonymous_user, demographic):
    endpoint = f"/api/v1/demographics/{demographic.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(demographic.id)
    assert response.data["name"] == demographic.name


@pytest.mark.django_db
def test_retrieve_demographic_errors(anonymous_user):
    endpoint = "/api/v1/demographics/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"


@pytest.mark.django_db
def test_create_demographic(contributor_user):
    endpoint = "/api/v1/demographics/"
    data = {"name": "New Demographic"}
    response = contributor_user.post(endpoint, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Demographic.objects.filter(name="New Demographic").exists()
    assert response.data["name"] == "New Demographic"


@pytest.mark.django_db
def test_create_demographic_errors(member_user):
    endpoint = "/api/v1/demographics/"
    data = {"name": "Unauthorized Demographic"}
    member_response = member_user.post(endpoint, data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post(endpoint, data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"
    assert not Demographic.objects.filter(name="Unauthorized Demographic").exists()


@pytest.mark.django_db
def test_update_demographic(contributor_user, demographic):
    endpoint = f"/api/v1/demographics/{demographic.id}/"
    data = {"name": "Updated Demographic"}
    response = contributor_user.put(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    demographic.refresh_from_db()
    assert demographic.name == "Updated Demographic"


@pytest.mark.django_db
def test_partial_update_demographic(contributor_user, demographic):
    endpoint = f"/api/v1/demographics/{demographic.id}/"
    data = {"name": "Partially Updated Demographic"}
    response = contributor_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    demographic.refresh_from_db()
    assert demographic.name == "Partially Updated Demographic"


@pytest.mark.django_db
def test_delete_demographic(contributor_user, demographic):
    assert demographic.is_available
    endpoint = f"/api/v1/demographics/{demographic.id}/"
    response = contributor_user.delete(endpoint)
    demographic.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Demographic.objects.filter(id=demographic.id).exists()
    assert not demographic.is_available


@pytest.mark.django_db
def test_search_demographic(member_user):
    DemographicFactory(name="Harem")
    DemographicFactory(name="Gore")
    DemographicFactory(name="Isekai")
    endpoint = "/api/v1/demographics/"

    response = member_user.get(endpoint, {"q": "Harem"})
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Harem"

    response_partial = member_user.get(endpoint, {"q": "Gore"})
    assert response_partial.status_code == status.HTTP_200_OK
    assert response_partial.reason_phrase == "OK"
    assert len(response_partial.data["results"]) == 1
    assert response_partial.data["results"][0]["name"] == "Gore"

    response_no_results = member_user.get(endpoint, {"q": "Music"})  # Not Found
    assert response_no_results.status_code == status.HTTP_200_OK
    assert response_no_results.reason_phrase == "OK"
    assert len(response_no_results.data["results"]) == 0
