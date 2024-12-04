"""Serializer Tests for Genres App."""

import pytest

from ...serializers import (
    GenreReadSerializer,
    GenreWriteSerializer,
    GenreMinimalSerializer,
    ThemeReadSerializer,
    ThemeWriteSerializer,
    DemographicReadSerializer,
    DemographicWriteSerializer,
)


@pytest.mark.django_db
class TestGenreSerializers:
    """Serializer tests for Genre model."""

    def test_genre_read_serializer(self, genre):
        serializer = GenreReadSerializer(genre)
        expected_data = {
            "id": str(genre.id),
            "name": genre.name,
            "slug": genre.slug,
            "created_at": genre.created_at.isoformat(),
            "updated_at": genre.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_genre_write_serializer_valid_data(self):
        data = {"name": "Action"}
        serializer = GenreWriteSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["name"] == "Action"

    def test_genre_write_serializer_invalid_data(self):
        data = {}
        serializer = GenreWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors

    def test_genre_minimal_serializer(self, genre):
        serializer = GenreMinimalSerializer(genre)
        expected_data = {
            "id": str(genre.id),
            "name": genre.name,
        }
        assert serializer.data == expected_data


@pytest.mark.django_db
class TestThemeSerializers:
    """Serializer tests for Theme model."""

    def test_theme_read_serializer(self, theme):
        serializer = ThemeReadSerializer(theme)
        expected_data = {
            "id": str(theme.id),
            "name": theme.name,
            "slug": theme.slug,
            "created_at": theme.created_at.isoformat(),
            "updated_at": theme.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_theme_write_serializer_valid_data(self):
        data = {"name": "Fantasy"}
        serializer = ThemeWriteSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["name"] == "Fantasy"

    def test_theme_write_serializer_invalid_data(self):
        data = {}
        serializer = ThemeWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors


@pytest.mark.django_db
class TestDemographicSerializers:
    """Serializer tests for Demographic model."""

    def test_demographic_read_serializer(self, demographic):
        serializer = DemographicReadSerializer(demographic)
        expected_data = {
            "id": str(demographic.id),
            "name": demographic.name,
            "slug": demographic.slug,
            "created_at": demographic.created_at.isoformat(),
            "updated_at": demographic.updated_at.isoformat(),
        }
        assert serializer.data == expected_data

    def test_demographic_write_serializer_valid_data(self):
        data = {"name": "Shounen"}
        serializer = DemographicWriteSerializer(data=data)
        assert serializer.is_valid()
        assert serializer.validated_data["name"] == "Shounen"

    def test_demographic_write_serializer_invalid_data(self):
        data = {}
        serializer = DemographicWriteSerializer(data=data)
        assert not serializer.is_valid()
        assert "name" in serializer.errors
