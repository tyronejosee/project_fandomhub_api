"""Model tests for Animes App."""

import pytest
from django.db import IntegrityError
from django.core.exceptions import ValidationError

# from apps.utils.functions import generate_test_image
from ...choices import DayChoices
from ..factories import BroadcastFactory, AnimeFactory


@pytest.mark.django_db
class TestBroadcastModel:
    """Tests for Broadcast model."""

    def test_broadcast_creation(self):
        broadcast = BroadcastFactory.create(day=DayChoices.FRIDAY)
        assert broadcast.day == "friday"
        assert broadcast.get_day_display() == "Friday"

    def test_field_string_max_length(self):
        broadcast = BroadcastFactory.create(string="a" * 51)  # Max 50
        with pytest.raises(ValidationError):
            broadcast.full_clean()


@pytest.mark.django_db
class TestAnimeModel:
    """Tests for Anime model."""

    def test_anime_creation(self):
        anime = AnimeFactory.create(name="Naruto Shippuden")
        assert anime.name == "Naruto Shippuden"
        assert str(anime) == "Naruto Shippuden"

    def test_field_name_unique(self):
        AnimeFactory.create(name="Boruto")
        with pytest.raises(IntegrityError):
            AnimeFactory.create(name="Boruto")

    def test_field_name_jpn_unique(self):
        AnimeFactory.create(name_jpn="モンスター")
        with pytest.raises(IntegrityError):
            AnimeFactory.create(name_jpn="モンスター")

    def test_field_name_rom_unique(self):
        AnimeFactory.create(name_rom="Monster")
        with pytest.raises(IntegrityError):
            AnimeFactory.create(name_rom="Monster")

    def test_field_string_max_length(self):
        anime = AnimeFactory.create(name="a" * 256)  # Max 255
        with pytest.raises(ValidationError):
            anime.full_clean()

    # def test_field_invalid_dimensions_image(self, anime):
    #     pass
