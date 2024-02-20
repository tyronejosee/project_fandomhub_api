"""Tests for Models in Contents App."""

from datetime import date
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.contents.models import Anime, Manga
from apps.categories.models import Studio, Genre, Season, Url, Demographic
from apps.persons.models import Author


class AnimeModelTestCase(TestCase):
    """Test cases for Anime model."""

    def setUp(self):
        # External models
        self.studio = Studio.objects.create(name="Studio Example")
        self.genre = Genre.objects.create(name="Genre Example")
        self.season = Season.objects.create(season=1, year=2024)
        self.author = Author.objects.create(name="Author Example")
        self.demographic = Demographic.objects.create(
            name="Demographic Example"
        )
        self.url = Url.objects.create(url="http://example.com")

        self.anime = Anime.objects.create(
            name="Name Example",
            name_jpn="Name JPN Example",
            image=None,
            synopsis="Synopsis Example",
            episodes=12,
            duration="24 min per Episode",
            release=date(2022, 1, 1),
            category=1,
            status=1,
            rating=1,
            studio_id=self.studio,
            season_id=self.season,
            mean=8.0,
            rank=1,
            popularity=100,
            num_list_users=1000,
            num_scoring_users=500
        )

        # Set ManyToManyField
        self.anime.genre_id.set([self.genre])
        self.anime.url_id.set([self.url])

    def test_creation(self):
        """Test creation of a Anime instance."""
        self.assertEqual(self.anime.name, "Name Example")
        self.assertEqual(self.anime.name_jpn, "Name JPN Example")
        self.assertEqual(self.anime.synopsis, "Synopsis Example")
        self.assertEqual(self.anime.episodes, 12)
        self.assertEqual(self.anime.duration, "24 min per Episode")
        self.assertEqual(self.anime.release, date(2022, 1, 1))
        self.assertEqual(self.anime.category, 1)
        self.assertEqual(self.anime.status, 1)
        self.assertEqual(self.anime.rating, 1)
        self.assertEqual(self.anime.studio_id, self.studio)
        self.assertEqual(self.anime.genre_id.first(), self.genre)
        self.assertEqual(self.anime.season_id, self.season)
        self.assertEqual(self.anime.url_id.first(), self.url)
        self.assertEqual(self.anime.mean, 8.0)
        self.assertEqual(self.anime.rank, 1)
        self.assertEqual(self.anime.popularity, 100)
        self.assertEqual(self.anime.num_list_users, 1000)
        self.assertEqual(self.anime.num_scoring_users, 500)

    def test_episodes_validation(self):
        """Test episodes field validation."""
        # Test negative episodes value
        with self.assertRaises(ValidationError):
            anime = Anime(
                name="Test Anime",
                name_jpn="Test Anime JP",
                episodes=-1
            )
            anime.full_clean()

        # Test episodes value over the maximum allowed
        with self.assertRaises(ValidationError):
            anime = Anime(
                name="Test Anime",
                name_jpn="Test Anime JP",
                episodes=1501
            )
            anime.full_clean()

        # Test valid episodes value
        anime = Anime(
            name="Test Anime",
            name_jpn="Test Anime JP",
            episodes=12
        )
        anime.full_clean()

    def test_str_method(self):
        """Test srt method."""
        anime = Anime.objects.get(name="Name Example")
        self.assertEqual(str(anime), "Name Example")

    def test_query(self):
        """Test querying for anime objects."""
        Anime.objects.create(
            name="Query Example One",
            name_jpn="Query Example One",
            episodes=12,
            category=1,
            status=1,
            rating=1,
        )
        Anime.objects.create(
            name="Query Example Two",
            name_jpn="Query Example Two",
            episodes=12,
            category=1,
            status=1,
            rating=1,
        )
        queried_animes = Anime.objects.filter(name__contains="Query")
        self.assertEqual(queried_animes.count(), 2)
        self.assertNotEqual(queried_animes.count(), 0)


class MangaModelTestCase(TestCase):
    """Test cases for Manga model."""

    def setUp(self):
        # External models
        self.genre = Genre.objects.create(name="Genre Example")
        self.season = Season.objects.create(season=1, year=2024)
        self.author = Author.objects.create(name="Author Example")
        self.demographic = Demographic.objects.create(
            name="Demographic Example"
        )
        self.url = Url.objects.create(url="http://example.com")

        self.manga = Manga.objects.create(
            name="Name Example",
            name_jpn="Name JPN Example",
            image=None,
            synopsis="Synopsis Example",
            chapters=50,
            release=date(2024, 1, 1),
            media_type=1,
            status=1,
            author_id=self.author,
            demographic_id=self.demographic,
            mean=8.0,
            rank=1,
            popularity=100,
            num_list_users=1000,
            num_scoring_users=500,
        )

        # Set ManyToManyField
        self.manga.genre_id.set([self.genre])
        self.manga.url_id.set([self.url])

    def test_manga_creation(self):
        """Test creation of a Manga instance."""
        self.assertEqual(self.manga.name, "Name Example")
        self.assertEqual(self.manga.name_jpn, "Name JPN Example")
        self.assertEqual(self.manga.synopsis, "Synopsis Example")
        self.assertEqual(self.manga.chapters, 50)
        self.assertEqual(self.manga.release, date(2024, 1, 1))
        self.assertEqual(self.manga.media_type, 1)
        self.assertEqual(self.manga.status, 1)
        self.assertEqual(self.manga.author_id, self.author)
        self.assertEqual(self.manga.demographic_id, self.demographic)
        self.assertEqual(self.manga.genre_id.first(), self.genre)
        self.assertEqual(self.manga.url_id.first(), self.url)
        self.assertEqual(self.manga.mean, 8.0)
        self.assertEqual(self.manga.rank, 1)
        self.assertEqual(self.manga.popularity, 100)
        self.assertEqual(self.manga.num_list_users, 1000)
        self.assertEqual(self.manga.num_scoring_users, 500)

    def test_chapters_validation(self):
        """Test chapters field validation."""
        # Test negative chapters value
        with self.assertRaises(ValidationError):
            manga = Manga(
                name="Test Manga",
                name_jpn="Test Manga JP",
                chapters=-1
            )
            manga.full_clean()

    def test_str_method(self):
        """Test srt method."""
        manga = Manga.objects.get(name="Name Example")
        self.assertEqual(str(manga), "Name Example")

    def test_manga_query(self):
        """Test querying for anime objects."""
        Manga.objects.create(
            name="Query Example One",
            name_jpn="Query Example One",
            chapters=50,
            media_type=1,
            status=1
        )
        Manga.objects.create(
            name="Query Example Two",
            name_jpn="Query Example Two",
            chapters=50,
            media_type=1,
            status=1,
        )
        queried_mangas = Manga.objects.filter(name__contains="Query")
        self.assertEqual(queried_mangas.count(), 2)
        self.assertNotEqual(queried_mangas.count(), 0)
