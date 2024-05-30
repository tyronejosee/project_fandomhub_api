"""Tests for Models in Contents App."""

from datetime import date
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.contents.models import Anime, Manga
from apps.categories.models import Studio, Genre, Theme, Season, Demographic
from apps.persons.models import Person


class AnimeModelTestCase(TestCase):
    """Test cases for Anime model."""

    def setUp(self):
        # External models
        self.studio = Studio.objects.create(name="OLM")
        self.genre = Genre.objects.create(name="Action")
        self.theme = Theme.objects.create(name="Gore")
        self.season = Season.objects.create(season="spring", year=1997)
        self.demographic = Demographic.objects.create(name="Seinen")

    def test_creation(self):
        """Test creation of a Anime instance."""
        anime = Anime.objects.create(
            name="Berserk",
            name_jpn="剣風伝奇ベルセルク",
            name_rom="Berserk",
            image=None,
            synopsis="Incapacitated...",
            episodes=25,
            duration="23 min. per ep.",
            release=date(1997, 10, 8),
            category="tv",
            website="https://www.vap.co.jp/berserk/tv.html",
            trailer="https://youtu.be/5g5uPsKDGYg",
            status="finished",
            rating=1,
            studio=self.studio,
            season=self.season,
            mean=8.0,
            rank=1,
            popularity=100,
            favorites=3,
            num_list_users=1000,
        )

        # Set ManyToManyField
        anime.genres.set([self.genre])
        anime.themes.set([self.theme])

        self.assertEqual(anime.name, "Berserk")
        self.assertEqual(anime.name_jpn, "剣風伝奇ベルセルク")
        self.assertEqual(anime.name_rom, "Berserk")
        self.assertEqual(anime.synopsis, "Incapacitated...")
        self.assertEqual(anime.episodes, 25)
        self.assertEqual(anime.duration, "23 min. per ep.")
        self.assertEqual(anime.release, date(1997, 10, 8))
        self.assertEqual(anime.category, "tv")
        self.assertEqual(anime.website, "https://www.vap.co.jp/berserk/tv.html")
        self.assertEqual(anime.trailer, "https://youtu.be/5g5uPsKDGYg")
        self.assertEqual(anime.status, "finished")
        self.assertEqual(anime.rating, 1)
        self.assertEqual(anime.studio, self.studio)
        self.assertEqual(anime.genres.first(), self.genre)
        self.assertEqual(anime.themes.first(), self.theme)
        self.assertEqual(anime.season, self.season)
        self.assertEqual(anime.mean, 8.0)
        self.assertEqual(anime.rank, 1)
        self.assertEqual(anime.popularity, 100)
        self.assertEqual(anime.favorites, 3)
        self.assertEqual(anime.num_list_users, 1000)

    def test_duplicate_anime_name(self):
        """Test for duplicate anime name."""
        with self.assertRaises(ValidationError):
            anime1 = Anime(
                name="Komi Can't Communicate",
                name_jpn="古見さんは、コミュ症です。",
                episodes=12,
            )
            anime1.save()

            anime2 = Anime(
                name="Komi Can't Communicate",
                name_jpn="古見さんは、コミュ症です。",
                episodes=12,
            )
            anime2.full_clean()  # Error

    def test_update_anime(self):
        """Test updating an anime."""
        anime = Anime(
            name="Dark Gathering",
            name_jpn="ダークギャザリング",
            studio=self.studio,
            episodes=25,
        )
        anime.save()

        anime.name = "Dark Gathering - Season 2"
        anime.full_clean()
        anime.save()

        updated_anime = Anime.objects.get(pk=anime.pk)
        self.assertEqual(updated_anime.name, "Dark Gathering - Season 2")

    def test_delete_anime(self):
        """Test deleting an anime."""
        anime = Anime(
            name="Summertime Render",
            name_jpn="サマータイムレンダ",
        )
        anime.save()
        anime.delete()
        with self.assertRaises(Anime.DoesNotExist):
            Anime.objects.get(pk=anime.pk)

    def test_validate_name_rom(self):
        """Test name_rom field validation."""
        anime = Anime.objects.create(
            name="Naruto", name_jpn="ナルト", name_rom=""  # Empty
        )
        self.assertEqual(anime.name_rom, "Naruto")
        self.assertEqual(anime.name, anime.name_rom)


class MangaModelTestCase(TestCase):
    """Test cases for Manga model."""

    def setUp(self):
        # External models
        self.genre = Genre.objects.create(name="Action")
        self.author = Person.objects.create(
            name="Fujimoto Tatsuki"
        )  # TODO: Add new fields
        self.demographic = Demographic.objects.create(name="Shounen")

    def test_manga_creation(self):
        """Test creation of a Manga instance."""
        manga = Manga.objects.create(
            name="Chainsaw Man",
            name_jpn="チェンソーマン",
            name_rom="Chainsaw Man",
            image=None,
            synopsis="Denji has...",
            chapters=97,
            release=date(2018, 12, 3),
            media_type=1,
            website="https://www.shonenjump.com/j/rensai/chainsaw.html",
            status=1,
            author=self.author,
            demographic=self.demographic,
            mean=8.0,
            rank=1,
            popularity=100,
            num_list_users=1000,
        )

        # Set ManyToManyField
        manga.genres.set([self.genre])

        self.assertEqual(manga.name, "Chainsaw Man")
        self.assertEqual(manga.name_jpn, "チェンソーマン")
        self.assertEqual(manga.name_rom, "Chainsaw Man")
        self.assertEqual(manga.synopsis, "Denji has...")
        self.assertEqual(manga.chapters, 97)
        self.assertEqual(manga.release, date(2018, 12, 3))
        self.assertEqual(manga.media_type, 1)
        self.assertEqual(
            manga.website, "https://www.shonenjump.com/j/rensai/chainsaw.html"
        )
        self.assertEqual(manga.status, 1)
        self.assertEqual(manga.author, self.author)
        self.assertEqual(manga.demographic, self.demographic)
        self.assertEqual(manga.genres.first(), self.genre)
        self.assertEqual(manga.mean, 8.0)
        self.assertEqual(manga.rank, 1)
        self.assertEqual(manga.popularity, 100)
        self.assertEqual(manga.num_list_users, 1000)

    def test_duplicate_manga_name(self):
        """Test for duplicate manga name."""
        with self.assertRaises(ValidationError):
            manga1 = Manga(
                name="Fire Punch",
                name_jpn="ファイアパンチ",
                author=self.author,
                chapters=83,
            )
            manga1.save()

            manga2 = Manga(
                name="Fire Punch",
                name_jpn="ファイアパンチ",
                author=self.author,
                chapters=83,
            )
            manga2.full_clean()  # Error

    def test_update_manga(self):
        """Test updating a manga."""
        manga = Manga(
            name="Goodbye, Ery", name_jpn="さよなら絵梨", author=self.author, chapters=1
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
        manga = Anime.objects.create(
            name="Monogatari Series: First Season",
            name_jpn="〈物語〉シリーズ ファーストシーズン",
            name_rom="",  # Empty
        )
        self.assertEqual(manga.name_rom, "Monogatari Series: First Season")
        self.assertEqual(manga.name, manga.name_rom)
