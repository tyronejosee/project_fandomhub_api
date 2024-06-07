"""Tests for Models in Mangas App."""

# from datetime import date
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.mangas.models import Manga
from apps.genres.models import Genre, Demographic
from apps.persons.models import Person


class MangaModelTestCase(TestCase):
    """Test cases for Manga model."""

    def setUp(self):
        # External models
        self.genre = Genre.objects.create(name="Action")
        self.author_id = Person.objects.create(
            name="Fujimoto Tatsuki"
        )  # TODO: Add new fields
        self.demographic_id = Demographic.objects.create(name="Shounen")

    def test_manga_creation(self):
        """Test creation of a Manga instance."""
        manga = Manga.objects.create(
            name="Chainsaw Man",
            name_jpn="チェンソーマン",
            name_rom="Chainsaw Man",
            image=None,
            synopsis="Denji has...",
            chapters=97,
            media_type=1,
            website="https://www.shonenjump.com/j/rensai/chainsaw.html",
            status=1,
            author=self.author_id,
            demographic=self.demographic_id,
            score=8.0,
            ranked=1,
            popularity=100,
            members=1000,
        )

        # Set ManyToManyField
        manga.genres.set([self.genre])

        self.assertEqual(manga.name, "Chainsaw Man")
        self.assertEqual(manga.name_jpn, "チェンソーマン")
        self.assertEqual(manga.name_rom, "Chainsaw Man")
        self.assertEqual(manga.synopsis, "Denji has...")
        self.assertEqual(manga.chapters, 97)
        self.assertEqual(manga.media_type, 1)
        self.assertEqual(
            manga.website, "https://www.shonenjump.com/j/rensai/chainsaw.html"
        )
        self.assertEqual(manga.status, 1)
        self.assertEqual(manga.author_id, self.author_id)
        self.assertEqual(manga.demographic_id, self.demographic_id)
        self.assertEqual(manga.genres.first(), self.genre)
        self.assertEqual(manga.score, 8.0)
        self.assertEqual(manga.ranked, 1)
        self.assertEqual(manga.popularity, 100)
        self.assertEqual(manga.members, 1000)

    def test_duplicate_manga_name(self):
        """Test for duplicate manga name."""
        with self.assertRaises(ValidationError):
            manga1 = Manga(
                name="Fire Punch",
                name_jpn="ファイアパンチ",
                author=self.author_id,
                chapters=83,
            )
            manga1.save()

            manga2 = Manga(
                name="Fire Punch",
                name_jpn="ファイアパンチ",
                author=self.author_id,
                chapters=83,
            )
            manga2.full_clean()  # Error

    def test_update_manga(self):
        """Test updating a manga."""
        manga = Manga(
            name="Goodbye, Ery",
            name_jpn="さよなら絵梨",
            author=self.author_id,
            chapters=1,
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
        )
        manga.save()
        manga.delete()
        with self.assertRaises(Manga.DoesNotExist):
            Manga.objects.get(pk=manga.pk)

    def test_validate_chapters(self):
        """Test chapters field validation."""
        with self.assertRaises(ValidationError):
            manga = Manga(
                name="Look Back", name_jpn="ルックバック", chapters=-1  # Negative
            )
            manga.full_clean()

    def test_validate_name_rom(self):
        """Test name_rom field validation."""
        manga = Manga.objects.create(
            name="Monogatari Series First Season",
            name_jpn="〈物語〉シリーズ ファーストシーズン",
            name_rom="",  # Empty
            chapters=4,
        )
        self.assertEqual(manga.name_rom, "Monogatari Series First Season")
        self.assertEqual(manga.name, manga.name_rom)
        self.assertEqual(manga.chapters, 4)
