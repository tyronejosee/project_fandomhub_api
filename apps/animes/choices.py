"""Choices for Animes App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class StatusChoices(TextChoices):

    PENDING = "pending", _("Pending")
    FINISHED = "finished", _("Finished")
    AIRING = "airing", _("Airing")
    UPCOMING = "upcoming", _("Upcoming")


class CategoryChoices(TextChoices):

    PENDING = "pending", _("Pending")
    TV = "tv", _("TV")
    OVA = "ova", _("OVA")
    MOVIE = "movie", _("Movie")
    SPECIAL = "special", _("Special")
    ONA = "ona", _("ONA")
    MUSIC = "music", _("Music")


class RatingChoices(TextChoices):

    PENDING = "pending", _("Pending")
    G = "g", _("G - All Ages")
    PG = "pg", _("PG - Children")
    PG13 = "pg13", _("PG-13 - Teens 13 and Older")
    R = "r", _("R - 17+ (Violence & Profanity)")
    RPLUS = "rplus", _("R+ - Profanity & Mild Nudity")
    RX = "rx", _("RX - Hentai")


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
