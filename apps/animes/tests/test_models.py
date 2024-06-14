"""Tests for Models in Animes App."""

from datetime import date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.producers.models import Producer
from apps.producers.choices import TypeChoices
from apps.genres.models import Genre, Theme, Demographic
from ..models import Anime
from ..choices import (
    StatusChoices,
    MediaTypeChoices,
    RatingChoices,
    SourceChoices,
    SeasonChoices,
)


class AnimeModelTestCase(TestCase):
    """Test cases for Anime model."""

    def setUp(self):
        # External models
        self.studio = Producer.objects.create(name="Generic", type=TypeChoices.STUDIO)
        self.genre = Genre.objects.create(name="Generic")
        self.theme = Theme.objects.create(name="Generic")
        self.demographic = Demographic.objects.create(name="Generic")

    def test_creation(self):
        """Test creation of an Anime instance."""
        anime = Anime.objects.create(
            name="Berserk",
            name_jpn="剣風伝奇ベルセルク",
            name_rom="Berserk",
            image=None,
            trailer="https://youtu.be/5g5uPsKDGYg",
            synopsis="Guts, a man who will...",
            background="Kenpuu Denki Berserk adapts...",
            season=SeasonChoices.FALL,
            year=1997,
            media_type=MediaTypeChoices.TV,
            source=SourceChoices.MANGA,
            episodes=25,
            status=StatusChoices.FINISHED,
            aired_from=date(1997, 10, 8),
            aired_to=date(1998, 4, 1),
            studio_id=self.studio,
            duration=timedelta(minutes=23),
            rating=RatingChoices.RPLUS,
            website="https://www.vap.co.jp/berserk/tv.html",
            is_recommended=True,
            score=8.5,
            ranked=92,
            popularity=311,
            members=666302,
            favorites=28020,
        )

        # Set ManyToManyField
        anime.genres.set([self.genre])
        anime.themes.set([self.theme])

        self.assertEqual(anime.name, "Berserk")
        self.assertEqual(anime.name_jpn, "剣風伝奇ベルセルク")
        self.assertEqual(anime.name_rom, "Berserk")
        self.assertEqual(anime.trailer, "https://youtu.be/5g5uPsKDGYg")
        self.assertEqual(anime.synopsis, "Guts, a man who will...")
        self.assertEqual(anime.background, "Kenpuu Denki Berserk adapts...")
        self.assertEqual(anime.season, SeasonChoices.FALL)
        self.assertEqual(anime.year, 1997)
        self.assertEqual(anime.media_type, "tv")
        self.assertEqual(anime.source, SourceChoices.MANGA)
        self.assertEqual(anime.episodes, 25)
        self.assertEqual(anime.status, StatusChoices.FINISHED)
        self.assertEqual(anime.aired_from, date(1997, 10, 8))
        self.assertEqual(anime.aired_to, date(1998, 4, 1))
        self.assertEqual(anime.studio_id, self.studio)
        self.assertEqual(anime.duration, timedelta(minutes=23))
        self.assertEqual(anime.rating, RatingChoices.RPLUS)
        self.assertEqual(anime.website, "https://www.vap.co.jp/berserk/tv.html")
        self.assertEqual(anime.is_recommended, True)
        self.assertEqual(anime.score, 8.5)
        self.assertEqual(anime.ranked, 92)
        self.assertEqual(anime.popularity, 311)
        self.assertEqual(anime.members, 666302)
        self.assertEqual(anime.favorites, 28020)

        self.assertEqual(anime.genres.first(), self.genre)
        self.assertEqual(anime.themes.first(), self.theme)

    def test_duplicate_anime_name(self):
        """Test for duplicate anime name."""
        anime1 = Anime(
            name="Komi Can't Communicate",
            name_jpn="古見さんは、コミュ症です。",
            episodes=12,
            season=SeasonChoices.FALL,
            year=2021,
            media_type=MediaTypeChoices.TV,
            source=SourceChoices.MANGA,
            status=StatusChoices.FINISHED,
            aired_from=date(2021, 10, 6),
            studio_id=self.studio,
            duration=timedelta(minutes=23),
            rating=RatingChoices.PG13,
        )
        anime1.save()

        with self.assertRaises(ValidationError):
            anime2 = Anime(
                name="Komi Can't Communicate",
                name_jpn="古見さんは、コミュ症です。",
                episodes=12,
                season=SeasonChoices.FALL,
                year=2021,
                media_type=MediaTypeChoices.TV,
                source=SourceChoices.MANGA,
                status=StatusChoices.FINISHED,
                aired_from=date(2021, 10, 6),
                studio_id=self.studio,
                duration=timedelta(minutes=23),
                rating=RatingChoices.PG13,
            )
            anime2.full_clean()  # Error

    def test_update_anime(self):
        """Test updating an anime."""
        anime = Anime(
            name="Dark Gathering",
            name_jpn="ダークギャザリング",
            episodes=25,
            season=SeasonChoices.SUMMER,
            year=2023,
            media_type=MediaTypeChoices.TV,
            source=SourceChoices.MANGA,
            status=StatusChoices.FINISHED,
            aired_from=date(2023, 7, 11),
            studio_id=self.studio,
            duration=timedelta(minutes=23),
            rating=RatingChoices.PG13,
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
            season=SeasonChoices.SPRING,
            year=2022,
            media_type=MediaTypeChoices.TV,
            source=SourceChoices.MANGA,
            status=StatusChoices.FINISHED,
            aired_from=date(2022, 4, 15),
            studio_id=self.studio,
            duration=timedelta(minutes=23),
            rating=RatingChoices.R,
        )
        anime.genres.set([self.genre])
        anime.themes.set([self.theme])
        anime.save()
        anime.delete()
        with self.assertRaises(Anime.DoesNotExist):
            Anime.objects.get(pk=anime.pk)

    def test_validate_name_rom(self):
        """Test name_rom field validation."""
        anime = Anime.objects.create(
            name="Naruto: Shippuuden",
            name_jpn="ナルト",
            name_rom="",  # Empty
            season=SeasonChoices.WINTER,
            year=2007,
            media_type=MediaTypeChoices.TV,
            source=SourceChoices.MANGA,
            status=StatusChoices.FINISHED,
            aired_from=date(2007, 2, 15),
            studio_id=self.studio,
            duration=timedelta(minutes=23),
            rating=RatingChoices.PG13,
        )
        self.assertEqual(anime.name_rom, "Naruto: Shippuuden")
        self.assertEqual(anime.name, anime.name_rom)
