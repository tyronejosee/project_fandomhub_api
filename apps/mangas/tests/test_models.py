"""Tests for Models in Mangas App."""

from datetime import date
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.genres.models import Genre, Demographic
from apps.persons.models import Person
from apps.persons.models import CategoryChoices
from ..models import Magazine, Manga
from ..choices import MediaTypeChoices, StatusChoices


class MangaModelTestCase(TestCase):
    """Test cases for Manga model."""

    def setUp(self):
        # External models
        self.genre = Genre.objects.create(name="Generic")
        self.author_id = Person.objects.create(
            name="Generic Artist", category=CategoryChoices.ARTIST, is_available=True
        )
        self.demographic_id = Demographic.objects.create(name="Generic")
        self.serialization_id = Magazine.objects.create(name="Generic")

    def test_manga_creation(self):
        """Test creation of a Manga instance."""
        manga = Manga.objects.create(
            name="Chainsaw Man",
            name_jpn="チェンソーマン",
            name_rom="Chainsaw Man",
            alternative_names=["Chainsaw-man", "CSM"],
            image=None,
            synopsis="Denji has...",
            background="As part of the JUMP START...",
            media_type=MediaTypeChoices.MANGA,
            chapters=97,
            volumes=11,
            status=StatusChoices.FINISHED,
            published_from=date(2018, 12, 3),
            published_to=date(2020, 12, 14),
            demographic_id=self.demographic_id,
            serialization_id=self.serialization_id,
            author_id=self.author_id,
            website="https://www.shonenjump.com/j/rensai/chainsaw.html",
            is_recommended=True,
            score=8.7,
            ranked=50,
            popularity=4,
            members=623310,
            favorites=82439,
        )

        # Set ManyToManyField
        manga.genres.set([self.genre])

        self.assertEqual(manga.name, "Chainsaw Man")
        self.assertEqual(manga.name_jpn, "チェンソーマン")
        self.assertEqual(manga.name_rom, "Chainsaw Man")
        self.assertEqual(manga.alternative_names, ["Chainsaw-man", "CSM"])
        self.assertEqual(manga.image, None),
        self.assertEqual(manga.synopsis, "Denji has...")
        self.assertEqual(manga.background, "As part of the JUMP START...")
        self.assertEqual(manga.media_type, MediaTypeChoices.MANGA)
        self.assertEqual(manga.chapters, 97)
        self.assertEqual(manga.volumes, 11)
        self.assertEqual(manga.status, StatusChoices.FINISHED)
        self.assertEqual(manga.published_from, date(2018, 12, 3))
        self.assertEqual(manga.published_to, date(2020, 12, 14))
        self.assertEqual(manga.demographic_id, self.demographic_id)
        self.assertEqual(manga.serialization_id, self.serialization_id)
        self.assertEqual(manga.author_id, self.author_id)
        self.assertEqual(
            manga.website, "https://www.shonenjump.com/j/rensai/chainsaw.html"
        )
        self.assertTrue(manga.is_recommended)
        self.assertEqual(manga.score, 8.7)
        self.assertEqual(manga.ranked, 50)
        self.assertEqual(manga.popularity, 4)
        self.assertEqual(manga.members, 623310)
        self.assertEqual(manga.favorites, 82439)
        self.assertEqual(manga.genres.first(), self.genre)

    def test_duplicate_manga_name(self):
        """Test for duplicate manga name."""
        with self.assertRaises(ValidationError):
            manga1 = Manga(
                name="Fire Punch",
                name_jpn="ファイアパンチ",
                chapters=83,
                volumes=8,
                status=StatusChoices.FINISHED,
                published_from=date(2016, 1, 18),
                author_id=self.author_id,
            )
            manga1.save()

            manga2 = Manga(
                name="Fire Punch",
                name_jpn="ファイアパンチ",
                chapters=83,
                volumes=8,
                published_from=date(2016, 1, 18),
                author_id=self.author_id,
            )
            manga2.full_clean()  # Error

    def test_update_manga(self):
        """Test updating a manga."""
        manga = Manga(
            name="Goodbye, Ery",
            name_jpn="さよなら絵梨",
            chapters=1,
            volumes=1,
            status=StatusChoices.FINISHED,
            published_from=date(2022, 4, 11),
            author_id=self.author_id,
        )
        manga.save()

        manga.name = "Goodbye, Eri"
        manga.full_clean()
        manga.save()
        updated_manga = Manga.objects.get(pk=manga.pk)
        self.assertEqual(updated_manga.name, "Goodbye, Eri")

    def test_delete_manga(self):
        """Test deleting a manga."""
        manga = Manga(
            name="Chainsaw Man: Buddy Stories",
            name_jpn="チェンソーマンバディ・ストーリーズ",
            chapters=4,
            volumes=1,
            status=StatusChoices.FINISHED,
            published_from=date(2021, 11, 4),
            author_id=self.author_id,
        )
        manga.save()
        manga.delete()
        with self.assertRaises(Manga.DoesNotExist):
            Manga.objects.get(pk=manga.pk)

    def test_validate_chapters(self):
        """Test chapters field validation."""
        with self.assertRaises(ValidationError):
            manga = Manga(
                name="Look Back",
                name_jpn="ルックバック",
                chapters=-1,  # Negative
                volumes=1,
                status=StatusChoices.FINISHED,
                published_from=date(2021, 7, 19),
                author_id=self.author_id,
            )
            manga.full_clean()

    def test_validate_name_rom(self):
        """Test name_rom field validation."""
        manga = Manga.objects.create(
            name="Monogatari Series First Season",
            name_jpn="〈物語〉シリーズ ファーストシーズン",
            name_rom="",  # Empty
            chapters=107,
            volumes=6,
            status=StatusChoices.FINISHED,
            published_from=date(2009, 7, 3),
            author_id=self.author_id,
        )
        self.assertEqual(manga.name_rom, "Monogatari Series First Season")
        self.assertEqual(manga.name, manga.name_rom)
        self.assertEqual(manga.chapters, 107)
