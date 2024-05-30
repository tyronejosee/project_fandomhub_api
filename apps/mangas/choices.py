"""Choices for Mangas App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class StatusChoices(TextChoices):

    PENDING = "pending", _("Pending")
    FINISHED = "finished", _("Finished")
    AIRING = "airing", _("Airing")
    UPCOMING = "upcoming", _("Upcoming")


class MediaTypeChoices(TextChoices):

    PENDING = "pending", _("Pending")
    MANGA = "manga", _("Manga")
    NOVEL = "novel", _("Novel")
    ONESHOT = "oneshot", _("One Shot")
    DOUJINSHI = "doujinshi", _("Doujinshi")
    MANHWA = "manhwa", _("Manhwa")
    OEL = "oel", _("OEL")


class SourceChoices(TextChoices):

    PENDING = "pending", _("Pending")
    ORIGINAL = "original", _("Original")
    MANGA = "manga", _("Manga")
    NOVEL = "novel", _("Novel")
    LNOVEL = "lnovel", _("Light Novel")
    VNOVEL = "vnovel", _("Visual Novel")
    GAME = "game", _("Game")
    BOOK = "book", _("Book")
    RADIO = "radio", _("Radio")
    MUSIC = "music", _("Music")
