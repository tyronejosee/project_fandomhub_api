"""Model Tests for Genres App."""

import pytest
from django.db import IntegrityError

from apps.genres.models import Genre, Theme, Demographic


@pytest.mark.django_db
class TestGenreModel:
    """Model tests for Genre model."""

    def test_genre_creation(self):
        genre = Genre.objects.create(name="Action")
        assert genre.name == "Action"
        assert str(genre) == "Action"

    def test_genre_unique_name(self):
        Genre.objects.create(name="Action")
        with pytest.raises(IntegrityError):
            Genre.objects.create(name="Action")

    def test_genre_slug_generation(self):
        genre = Genre.objects.create(name="Action")
        assert genre.slug == "action"

    def test_filter_by_name_prefix(self):
        Genre.objects.create(name="Action")
        Genre.objects.create(name="Adventure")
        Genre.objects.create(name="Comedy", is_available=False)
        results = Genre.objects.get_available()
        assert results.count() == 2


@pytest.mark.django_db
class TestThemeModel:
    """Model tests for Theme model."""

    def test_theme_creation(self):
        theme = Theme.objects.create(name="Gore")
        assert theme.name == "Gore"
        assert str(theme) == "Gore"

    def test_theme_unique_name(self):
        Theme.objects.create(name="Gore")
        with pytest.raises(IntegrityError):
            Theme.objects.create(name="Gore")

    def test_theme_slug_generation(self):
        theme = Theme.objects.create(name="Gore")
        assert theme.slug == "gore"


@pytest.mark.django_db
class TestDemographicModel:
    """Model tests for Demographic model."""

    def test_demographic_creation(self):
        demographic = Demographic.objects.create(name="Shounen")
        assert demographic.name == "Shounen"
        assert str(demographic) == "Shounen"

    def test_demographic_unique_name(self):
        Demographic.objects.create(name="Shounen")
        with pytest.raises(IntegrityError):
            Demographic.objects.create(name="Shounen")

    def test_demographic_slug_generation(self):
        demographic = Demographic.objects.create(name="Shounen")
        assert demographic.slug == "shounen"
