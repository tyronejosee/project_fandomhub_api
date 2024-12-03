"""Serializer Tests for Persons App."""

import pytest

from ...serializers import (
    PersonReadSerializer,
    PersonWriteSerializer,
    PersonMinimalSerializer,
    StaffMinimalSerializer,
)


@pytest.mark.django_db
class TestPersonSerializers:
    """Tests for Person serializers."""

    def test_person_read_serializer(self, person):
        serializer = PersonReadSerializer(person)
        expected_data = {
            "id": str(person.id),
            "name": person.name,
            "slug": person.slug,
            "given_name": person.given_name,
            "family_name": person.family_name,
            "image": person.image.url,
            "alternate_names": person.alternate_names,
            "birthday": person.birthday.isoformat(),
            "about": person.about,
            "website": person.website,
            "language": person.get_language_display(),
            "category": person.get_category_display(),
            "favorites": person.favorites,
            "created_at": person.created_at.isoformat(),
            "updated_at": person.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_person_write_serializer_valid_data(self, person):
        data = {
            "name": "Tatsuki Fujimoto",
            "given_name": person.given_name,
            "family_name": person.family_name,
            "image": person.image,
            "alternate_names": person.alternate_names,
            "birthday": person.birthday,
            "about": person.about,
            "website": person.website,
            "language": person.language,
            "category": person.category,
        }
        serializer = PersonWriteSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["name"] == "Tatsuki Fujimoto"

    def test_person_write_serializer_invalid_data(self):
        data = {}
        serializer = PersonWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors
        assert "image" in serializer.errors
        assert "category" in serializer.errors

    def test_person_minimal_serializer(self, person):
        serializer = PersonMinimalSerializer(person)
        expected_data = {
            "id": str(person.id),
            "name": person.name,
            "image": person.image.url,
            "language": person.get_language_display(),
            "favorites": person.favorites,
        }
        assert serializer.data == expected_data

    def test_staff_minimal_serializer(self, person):
        serializer = StaffMinimalSerializer(person)
        expected_data = {
            "id": str(person.id),
            "name": person.name,
            "image": person.image.url,
            "category": person.get_category_display(),
        }
        assert serializer.data == expected_data
