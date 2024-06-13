"""Tests for Models in Animes App."""

from datetime import date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.animes.models import Anime
from apps.producers.models import Producer
from apps.producers.choices import TypeChoices
from apps.genres.models import Genre, Theme, Demographic


class AnimeModelTestCase(TestCase):
    """Test cases for Anime model."""

    def setUp(self):
        # External models
        self.studio = Producer.objects.create(name="OLM", type=TypeChoices.STUDIO)
        self.genre = Genre.objects.create(name="Action")
        self.theme = Theme.objects.create(name="Gore")
        self.demographic = Demographic.objects.create(name="Seinen")
        # self.broadcast = Broadcast.objects.create(
        #     day="monday", time="20:00:00", timezone="JST"
        # )

    def test_creation(self):
        """Test creation of an Anime instance."""
        anime = Anime.objects.create(
            name="Berserk",
            name_jpn="剣風伝奇ベルセルク",
            name_rom="Berserk",
            image=None,
            synopsis="Incapacitated...",
            episodes=25,
            duration=timedelta(minutes=23),
            aired_from=date(1997, 10, 8),
            media_type="tv",
            website="https://www.vap.co.jp/berserk/tv.html",
            trailer="https://youtu.be/5g5uPsKDGYg",
            status="finished",
            rating="pg13",
            studio_id=self.studio,
            score=8.0,
            ranked=1,
            popularity=100,
            favorites=3,
            members=1000,
            # broadcast_id=self.broadcast,
        )

        # Set ManyToManyField
        anime.genres.set([self.genre])
        anime.themes.set([self.theme])

        self.assertEqual(anime.name, "Berserk")
        self.assertEqual(anime.name_jpn, "剣風伝奇ベルセルク")
        self.assertEqual(anime.name_rom, "Berserk")
        self.assertEqual(anime.synopsis, "Incapacitated...")
        self.assertEqual(anime.episodes, 25)
        self.assertEqual(anime.duration, timedelta(minutes=23))
        self.assertEqual(anime.aired_from, date(1997, 10, 8))
        self.assertEqual(anime.media_type, "tv")
        self.assertEqual(anime.website, "https://www.vap.co.jp/berserk/tv.html")
        self.assertEqual(anime.trailer, "https://youtu.be/5g5uPsKDGYg")
        self.assertEqual(anime.status, "finished")
        self.assertEqual(anime.rating, "pg13")
        self.assertEqual(anime.studio_id, self.studio)
        self.assertEqual(anime.genres.first(), self.genre)
        self.assertEqual(anime.themes.first(), self.theme)
        self.assertEqual(anime.score, 8.0)
        self.assertEqual(anime.ranked, 1)
        self.assertEqual(anime.popularity, 100)
        self.assertEqual(anime.favorites, 3)
        self.assertEqual(anime.members, 1000)
        # self.assertEqual(anime.broadcast_id, self.broadcast)

    def test_duplicate_anime_name(self):
        """Test for duplicate anime name."""
        anime1 = Anime(
            name="Komi Can't Communicate",
            name_jpn="古見さんは、コミュ症です。",
            episodes=12,
            aired_from=date(2021, 10, 6),
        )
        anime1.save()

        with self.assertRaises(ValidationError):
            anime2 = Anime(
                name="Komi Can't Communicate",
                name_jpn="古見さんは、コミュ症です。",
                episodes=12,
                aired_from=date(2021, 10, 6),
            )
            anime2.full_clean()  # Error

    def test_update_anime(self):
        """Test updating an anime."""
        anime = Anime(
            name="Dark Gathering",
            name_jpn="ダークギャザリング",
            studio_id=self.studio,
            episodes=25,
            aired_from=date(2023, 7, 11),
            duration="30 min",
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
            aired_from=date(2022, 4, 15),
        )
        anime.save()
        anime.delete()
        with self.assertRaises(Anime.DoesNotExist):
            Anime.objects.get(pk=anime.pk)

    def test_validate_name_rom(self):
        """Test name_rom field validation."""
        anime = Anime.objects.create(
            name="Naruto",
            name_jpn="ナルト",
            name_rom="",
            aired_from=date(2002, 10, 3),  # Empty
        )
        self.assertEqual(anime.name_rom, "Naruto")
        self.assertEqual(anime.name, anime.name_rom)
