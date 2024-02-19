"""Tests for Models in Contents App."""

from django.test import TestCase
from datetime import date
from apps.contents.models import Anime, Manga
from apps.categories.models import Studio, Genre, Season, Url, Demographic
from apps.persons.models import Author


class ContentModelsTest(TestCase):
    """Test cases for models."""

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

    # Anime Model
    def test_anime_creation(self):
        """Test creation of a Anime instance."""
        anime = Anime.objects.create(
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

        anime.genre_id.set([self.genre])
        anime.url_id.set([self.url])

        self.assertEqual(anime.name, "Name Example")
        self.assertEqual(anime.name_jpn, "Name JPN Example")
        self.assertEqual(anime.synopsis, "Synopsis Example")
        self.assertEqual(anime.episodes, 12)
        self.assertEqual(anime.duration, "24 min per Episode")
        self.assertEqual(anime.release, date(2022, 1, 1))
        self.assertEqual(anime.category, 1)
        self.assertEqual(anime.status, 1)
        self.assertEqual(anime.rating, 1)
        self.assertEqual(anime.studio_id, self.studio)
        self.assertEqual(anime.genre_id.first(), self.genre)
        self.assertEqual(anime.season_id, self.season)
        self.assertEqual(anime.url_id.first(), self.url)
        self.assertEqual(anime.mean, 8.0)
        self.assertEqual(anime.rank, 1)
        self.assertEqual(anime.popularity, 100)
        self.assertEqual(anime.num_list_users, 1000)
        self.assertEqual(anime.num_scoring_users, 500)

    def test_anime_query(self):
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

    # Manga Model
    def test_manga_creation(self):
        """Test creation of a Manga instance."""
        manga = Manga.objects.create(
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

        manga.genre_id.set([self.genre])
        manga.url_id.set([self.url])

        self.assertEqual(manga.name, "Name Example")
        self.assertEqual(manga.name_jpn, "Name JPN Example")
        self.assertEqual(manga.synopsis, "Synopsis Example")
        self.assertEqual(manga.chapters, 50)
        self.assertEqual(manga.release, date(2024, 1, 1))
        self.assertEqual(manga.media_type, 1)
        self.assertEqual(manga.status, 1)
        self.assertEqual(manga.author_id, self.author)
        self.assertEqual(manga.demographic_id, self.demographic)
        self.assertEqual(manga.genre_id.first(), self.genre)
        self.assertEqual(manga.url_id.first(), self.url)
        self.assertEqual(manga.mean, 8.0)
        self.assertEqual(manga.rank, 1)
        self.assertEqual(manga.popularity, 100)
        self.assertEqual(manga.num_list_users, 1000)
        self.assertEqual(manga.num_scoring_users, 500)

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
