"""Endpoints Tests for Producers App."""

import pytest
from rest_framework import status

from apps.utils.functions import generate_test_image
from apps.animes.tests.factories import AnimeFactory
from ..factories import ProducerFactory
from ...models import Producer
from ...choices import TypeChoices


@pytest.mark.django_db
def test_list_producers(anonymous_user, producer):
    endpoint = "/api/v1/producers/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_producer(anonymous_user, producer):
    endpoint = f"/api/v1/producers/{producer.id}/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert str(response.data["id"]) == str(producer.id)
    assert response.data["name"] == producer.name


@pytest.mark.django_db
def test_retrieve_producer_errors(anonymous_user):
    endpoint = "/api/v1/producers/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    response = anonymous_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "Not found."


@pytest.mark.django_db
def test_create_producer(contributor_user):
    image = generate_test_image(size=(600, 600))
    endpoint = "/api/v1/producers/"
    data = {
        "name": "New Producer",
        "name_jpn": "新しいプロデューサー",
        "about": "This is a description about the new producer.",
        "established": "2020",
        "type": TypeChoices.LICENSOR,
        "image": image,
    }
    response = contributor_user.post(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.reason_phrase == "Created"
    assert Producer.objects.filter(name="New Producer").exists()
    assert response.data["name"] == "New Producer"
    assert response.data["type"] == TypeChoices.LICENSOR


@pytest.mark.django_db
def test_create_producer_errors(member_user):
    image = generate_test_image(size=(600, 600))
    endpoint = "/api/v1/producers/"
    data = {
        "name": "Unauthorized Producer",
        "name_jpn": "新しいプロデューサー",
        "about": "This is a description about the new producer.",
        "established": "2020",
        "type": TypeChoices.LICENSOR,
        "image": image,
    }
    member_response = member_user.post(endpoint, data, format="multipart")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    assert member_response.reason_phrase == "Forbidden"
    member_user.logout()
    anonymus_response = member_user.post(endpoint, data, format="multipart")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED
    assert anonymus_response.reason_phrase == "Unauthorized"
    assert not Producer.objects.filter(name="Unauthorized Producer").exists()


@pytest.mark.django_db
def test_update_producer(contributor_user, producer):
    endpoint = f"/api/v1/producers/{producer.id}/"
    data = {
        "name": "Updated Producer",
        "name_jpn": producer.name_jpn,
        "about": producer.about,
        "established": producer.established,
        "type": producer.type,
        "image": producer.image,
    }
    response = contributor_user.put(endpoint, data, format="multipart")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    producer.refresh_from_db()
    assert producer.name == "Updated Producer"


@pytest.mark.django_db
def test_partial_update_producer(contributor_user, producer):
    endpoint = f"/api/v1/producers/{producer.id}/"
    data = {"name": "Partially Updated Producer"}
    response = contributor_user.patch(endpoint, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    producer.refresh_from_db()
    assert producer.name == "Partially Updated Producer"


@pytest.mark.django_db
def test_delete_producer(contributor_user, producer):
    assert producer.is_available
    endpoint = f"/api/v1/producers/{producer.id}/"
    response = contributor_user.delete(endpoint)
    producer.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.reason_phrase == "No Content"
    assert Producer.objects.filter(id=producer.id).exists()
    assert not producer.is_available


@pytest.mark.django_db
def test_search_field_name(member_user):
    ProducerFactory(name="Kyoto Animation")
    ProducerFactory(name="MAPPA")
    ProducerFactory(name="Madhouse")
    endpoint = "/api/v1/producers/"

    response = member_user.get(endpoint, {"q": "Kyoto Animation"})
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["name"] == "Kyoto Animation"

    response_partial = member_user.get(endpoint, {"q": "MAPPA"})
    assert response_partial.status_code == status.HTTP_200_OK
    assert response_partial.reason_phrase == "OK"
    assert len(response_partial.data["results"]) == 1
    assert response_partial.data["results"][0]["name"] == "MAPPA"

    response_no_results = member_user.get(endpoint, {"q": "Wit Studio"})  # Not Found
    assert response_no_results.status_code == status.HTTP_200_OK
    assert response_no_results.reason_phrase == "OK"
    assert len(response_no_results.data["results"]) == 0


@pytest.mark.django_db
def test_filter_order_by(member_user):
    ProducerFactory(name="A", favorites=900)
    ProducerFactory(name="J", favorites=500)
    ProducerFactory(name="Z", favorites=100)
    endpoint = "/api/v1/producers/"
    response = member_user.get(endpoint, {"order_by": "favorites"})
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert len(response.data["results"]) == 3
    assert [producer["favorites"] for producer in response.data["results"]] == [
        100,
        500,
        900,
    ]


@pytest.mark.django_db
def test_list_animes_by_producer(member_user):
    producer = ProducerFactory.create(type=TypeChoices.STUDIO)
    AnimeFactory.create(studio_id=producer)
    AnimeFactory.create(studio_id=producer)
    endpoint = f"/api/v1/producers/{producer.id}/animes/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_200_OK
    assert response.reason_phrase == "OK"
    assert "results" in response.data
    assert len(response.data["results"]) == 2
    assert response.data["count"] == 2


@pytest.mark.django_db
def test_list_animes_by_producer_error(member_user):
    producer = ProducerFactory.create(type=TypeChoices.STUDIO)
    endpoint = f"/api/v1/producers/{producer.id}/animes/"
    response = member_user.get(endpoint)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.reason_phrase == "Not Found"
    assert response.data["detail"] == "No animes found for this studio."
