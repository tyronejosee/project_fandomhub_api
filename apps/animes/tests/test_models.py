"""Tests for Models in Animes App."""

from datetime import date
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.animes.models import Anime
from apps.categories.models import Theme, Demographic
from apps.studios.models import Studio
from apps.genres.models import Genre
from apps.seasons.models import Season


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
