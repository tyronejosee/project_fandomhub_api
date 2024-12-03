"""Model Tests for Mangas App."""

import pytest
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from apps.utils.functions import generate_test_image
from ...models import Magazine, Manga


@pytest.mark.django_db
class TestMagazineModel:
    """Tests for Magazine model."""

    def test_magazine_creation(self):
        magazine = Magazine.objects.create(name="Weekly Shonen Magazine")
        assert magazine.name == "Weekly Shonen Magazine"
        assert str(magazine) == "Weekly Shonen Magazine"

    def test_magazine_unique_name(self):
        Magazine.objects.create(name="Shonen Jump")
        with pytest.raises(IntegrityError):
            Magazine.objects.create(name="Shonen Jump")

    def test_magazine_slug_generation(self):
        magazine = Magazine.objects.create(name="Monthly Afternoon")
        assert magazine.slug == "monthly-afternoon"

    def test_filter_by_name_prefix(self):
        Magazine.objects.create(name="Comic Beam")
        Magazine.objects.create(name="CoroCoro Comic")
        Magazine.objects.create(name="Hana to Yume", is_available=False)
        results = Magazine.objects.get_available()
        assert results.count() == 2


@pytest.mark.django_db
class TestMangaModel:
    """Tests for Manga model."""

    def test_manga_creation(self, manga):
        manga = Manga.objects.create(
            name="Oyasumi Punpun",
            name_jpn="おやすみプンプン",
            image=manga.image,
            synopsis=manga.synopsis,
            background=manga.background,
            media_type=manga.media_type,
            volumes=manga.volumes,
            chapters=manga.chapters,
            status=manga.status,
            published_from=manga.published_from,
            published_to=manga.published_to,
            demographic_id=manga.demographic_id,
            serialization_id=manga.serialization_id,
            author_id=manga.author_id,
            website=manga.website,
        )
        manga.genres.set(manga.genres.all())
        manga.themes.set(manga.themes.all())
        assert manga.name == "Oyasumi Punpun"
        assert str(manga) == "Oyasumi Punpun"

    def test_manga_unique_name(self, manga):
        Manga.objects.create(
            name="Kaguya-sama: Love is War",
            name_jpn="かぐや様は告らせたい～天才たちの恋愛頭脳戦～",
            published_from=manga.published_from,
            author_id=manga.author_id,
        )
        with pytest.raises(IntegrityError):
            Manga.objects.create(
                name="Kaguya-sama: Love is War",
                name_jpn="かぐや様は告らせたい～天才たちの恋愛頭脳戦～",
                published_from=manga.published_from,
                author_id=manga.author_id,
            )

    def test_manga_slug_generation(self, manga):
        manga = Manga.objects.create(
            name="3-gatsu no Lion",
            name_jpn="かぐや様は告らせたい～天才たちの恋愛頭脳戦～",
            published_from=manga.published_from,
            author_id=manga.author_id,
        )
        assert manga.slug == "3-gatsu-no-lion"

    def test_field_invalid_dimensions_image(self, manga):
        oversized_image = generate_test_image(size=(1000, 1300))
        manga = Manga(
            name="Oversized Manga",
            name_jpn="オーバーサイズ漫画",
            published_from=manga.published_from,
            author_id=manga.author_id,
        )
        with pytest.raises(ValidationError):
            manga.image.save("oversized_manga.jpg", oversized_image)
            manga.full_clean()
