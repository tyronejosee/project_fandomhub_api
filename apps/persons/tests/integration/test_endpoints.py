"""Endpoint Tests for Persons App."""

import pytest
from django.contrib.contenttypes.models import ContentType
from rest_framework import status

from apps.characters.tests.factories import CharacterVoiceFactory
from apps.mangas.tests.factories import MangaFactory
from apps.utils.tests.factories import PictureFactory
from ...models import Person
from ...choices import CategoryChoices
from ..factories import PersonFactory


@pytest.mark.django_db
def test_list_persons(anonymous_user, person):
    endpoint = "/api/v1/persons/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) > 0


@pytest.mark.django_db
def test_list_persons_errors(anonymous_user):
    endpoint = "/api/v1/persons/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"


@pytest.mark.django_db
def test_retrieve_person(anonymous_user, person):
    endpoint = f"/api/v1/persons/{person.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(person.id)
    assert response.data["name"] == person.name


@pytest.mark.django_db
def test_retrieve_person_errors(anonymous_user):
    person_id = "989423d1-d6c0-431a-8f62-d805b8a5f321"
    endpoint = f"/api/v1/persons/{person_id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"


@pytest.mark.django_db
def test_create_person(contributor_user, person):
    endpoint = "/api/v1/persons/"
    data = {
        "name": "New Person",
        "given_name": person.given_name,
        "family_name": person.family_name,
        "image": person.image,
        "birthday": person.birthday,
        "about": person.about,
        "website": person.website,
        "language": person.language,
        "category": person.category,
    }
    response = contributor_user.post(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Person.objects.filter(name="New Person").exists()
    assert response.data["name"] == "New Person"


@pytest.mark.django_db
def test_create_person_errors(member_user):
    endpoint = "/api/v1/persons/"
    data = {}
    member_response = member_user.post(endpoint, data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post(endpoint, data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"


@pytest.mark.django_db
def test_update_person(contributor_user, person):
    endpoint = f"/api/v1/persons/{person.id}/"
    data = {
        "name": "Updated Person",
        "given_name": person.given_name,
        "family_name": person.family_name,
        "image": person.image,
        "birthday": person.birthday,
        "about": person.about,
        "website": person.website,
        "language": person.language,
        "category": person.category,
    }
    response = contributor_user.put(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    person.refresh_from_db()
    assert person.name == "Updated Person"


@pytest.mark.django_db
def test_partial_update_person(contributor_user, person):
    endpoint = f"/api/v1/persons/{person.id}/"
    data = {"name": "Partially Updated Person"}
    response = contributor_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    person.refresh_from_db()
    assert person.name == "Partially Updated Person"


@pytest.mark.django_db
def test_delete_person(contributor_user, person):
    assert person.is_available
    endpoint = f"/api/v1/persons/{person.id}/"
    response = contributor_user.delete(endpoint)
    person.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Person.objects.filter(id=person.id).exists()
    assert not person.is_available


@pytest.mark.django_db
def test_list_mangas_by_person(anonymous_user):
    person = PersonFactory(category=CategoryChoices.WRITER)
    MangaFactory.create_batch(5, author_id=person)
    endpoint = f"/api/v1/persons/{person.id}/mangas/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert response.data["count"] == 5
    assert len(response.data["results"]) == 5


@pytest.mark.django_db
def test_list_mangas_by_person_errors(anonymous_user):
    person = PersonFactory(category=CategoryChoices.WRITER)
    endpoint = f"/api/v1/persons/{person.id}/mangas/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No mangas found for this person."


@pytest.mark.django_db
def test_list_pictures_by_manga(anonymous_user, person):
    PictureFactory.create_batch(
        3,
        content_type=ContentType.objects.get_for_model(Person),
        object_id=person.id,
    )
    endpoint = f"/api/v1/persons/{person.id}/pictures/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_pictures_by_person_errors(anonymous_user, person):
    endpoint = f"/api/v1/persons/{person.id}/pictures/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No pictures found for this person."


@pytest.mark.django_db
def test_create_image_by_person(contributor_user, person, picture):
    endpoint = f"/api/v1/persons/{person.id}/create-picture/"
    data = {
        "name": "New person image",
        "image": picture.image,
    }
    response = contributor_user.post(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert response.data["detail"] == "Picture uploaded successfully."


@pytest.mark.django_db
def test_list_voices_by_person(anonymous_user, person):
    CharacterVoiceFactory.create_batch(3, voice_id=person)
    endpoint = f"/api/v1/persons/{person.id}/voices/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data) == 3


@pytest.mark.django_db
def test_list_voices_by_person_errors(anonymous_user, person):
    endpoint = f"/api/v1/persons/{person.id}/voices/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No relations found for this person."
