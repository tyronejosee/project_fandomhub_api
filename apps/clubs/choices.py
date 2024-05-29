"""Choices for Clubs App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class CategoryChoices(TextChoices):

    ANIME = "anime", _("Anime")
    MANGA = "manga", _("Manga")
    ACTORS_AND_ARTISTS = "actors_and_artists", _("Actors and Artists")
    CHARACTERS = "characters", _("Characters")
    CITIES_AND_NEIGHBORHOODS = "cities_and_neighborhoods", _("Cities and Neighborhoods")
    COMPANIES = "companies", _("Companies")
    CONVENTIONS = "conventions", _("Conventions")
    GAMES = "games", _("Games")
    JAPAN = "japan", _("Japan")
    MUSIC = "music", _("Music")
    SCHOOLS = "schools", _("Schools")
    OTHER = "other", _("Other")
