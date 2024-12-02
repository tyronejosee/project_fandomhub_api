"""Endpoint Tests for Animes App."""

import pytest
from django.contrib.contenttypes.models import ContentType
from rest_framework import status

from apps.animes.tests.factories import AnimeFactory
from apps.animes.serializers import AnimeMinimalSerializer
from apps.mangas.tests.factories import MangaFactory
from apps.mangas.serializers import MangaMinimalSerializer
from apps.persons.tests.factories import PersonFactory
from apps.persons.models import Person
from apps.persons.serializers import PersonMinimalSerializer
from apps.utils.tests.factories import PictureFactory
from apps.utils.models import Picture
from apps.utils.serializers import PictureReadSerializer
from ...models import Character, CharacterVoice
from ..factories import (
    CharacterVoiceFactory,
    CharacterAnimeFactory,
    CharacterMangaFactory,
)


@pytest.mark.django_db
def test_list_character(anonymous_user, character):
    response = anonymous_user.get("/api/v1/characters/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    assert len(response.data["results"]) > 0


@pytest.mark.django_db
def test_retrieve_character(anonymous_user, character):
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert str(response.data["id"]) == str(character.id)
    assert response.data["name"] == character.name


@pytest.mark.django_db
def test_retrieve_character_errors(anonymous_user):
    response = anonymous_user.get(
        "/api/v1/characters/989423d1-d6c0-431a-8f62-d805b8a5f321/"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "Not found."


@pytest.mark.django_db
def test_create_character(contributor_user, character):
    data = {
        "name": "Makoto",
        "name_kanji": character.name_kanji,
        "about": character.about,
        "role": character.role,
        "image": character.image,
    }
    response = contributor_user.post("/api/v1/characters/", data, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert Character.objects.filter(name="Makoto").exists()
    assert response.data["name"] == "Makoto"


@pytest.mark.django_db
def test_create_character_unauthorized(member_user):
    data = {}
    member_response = member_user.post("/api/v1/characters/", data, format="json")
    assert member_response.status_code == status.HTTP_403_FORBIDDEN
    member_user.logout()
    anonymus_response = member_user.post("/api/v1/characters/", data, format="json")
    assert anonymus_response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_update_character(contributor_user, character):
    data = {
        "name": "Updated Character",
        "name_kanji": character.name_kanji,
        "about": character.about,
        "role": character.role,
        "image": character.image,
    }
    response = contributor_user.put(
        f"/api/v1/characters/{character.id}/", data, format="multipart"
    )
    assert response.status_code == status.HTTP_200_OK
    character.refresh_from_db()
    assert character.name == "Updated Character"


@pytest.mark.django_db
def test_partial_update_character(contributor_user, character):
    data = {"name": "Partially Updated Character"}
    response = contributor_user.patch(
        f"/api/v1/characters/{character.id}/", data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    character.refresh_from_db()
    assert character.name == "Partially Updated Character"


@pytest.mark.django_db
def test_delete_character(contributor_user, character):
    assert character.is_available
    response = contributor_user.delete(f"/api/v1/characters/{character.id}/")
    character.refresh_from_db()
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Character.objects.filter(id=character.id).exists()
    assert not character.is_available


@pytest.mark.django_db
def test_list_pictures_by_character(anonymous_user, character):
    picture = PictureFactory(
        content_type=ContentType.objects.get_for_model(Character),
        object_id=character.id,
    )
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/pictures/")
    expected_data = PictureReadSerializer([picture], many=True).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_list_pictures_by_character_errors(anonymous_user, character):
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/pictures/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert (
        response.data["detail"]
        == "There is no pictures associated with this character."
    )


@pytest.mark.django_db
def test_create_picture_by_character(contributor_user, character):
    data = {
        "name": "Momo Ayase",
        "image": character.image,
    }
    response = contributor_user.post(
        f"/api/v1/characters/{character.id}/pictures/create/",
        data,
        format="multipart",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Picture.objects.filter(name="Momo Ayase").exists()
    assert response.data["detail"] == "Picture uploaded successfully."


@pytest.mark.django_db
def test_list_voices_by_character(anonymous_user, character):
    staff_one = PersonFactory()
    staff_two = PersonFactory()
    CharacterVoiceFactory(voice_id=staff_one, character_id=character)
    CharacterVoiceFactory(voice_id=staff_two, character_id=character)
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/voices/")
    voices_ids = CharacterVoice.objects.filter(character_id=character.id).values_list(
        "voice_id", flat=True
    )
    voice = Person.objects.filter(id__in=voices_ids)
    expected_data = PersonMinimalSerializer(voice, many=True).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_retrieve_anime_by_character(anonymous_user, character):
    anime = AnimeFactory()
    CharacterAnimeFactory(character_id=character, anime_id=anime)
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/anime/")
    expected_data = AnimeMinimalSerializer(anime).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_retrieve_anime_by_character_not_found(anonymous_user, character):
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/anime/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "No anime found for this character."


@pytest.mark.django_db
def test_retrieve_manga_by_character(anonymous_user, character):
    manga = MangaFactory()
    CharacterMangaFactory(character_id=character, manga_id=manga)
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/manga/")
    expected_data = MangaMinimalSerializer(manga).data
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


@pytest.mark.django_db
def test_retrieve_manga_by_character_not_found(anonymous_user, character):
    response = anonymous_user.get(f"/api/v1/characters/{character.id}/manga/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data["detail"] == "No manga found for this character."
