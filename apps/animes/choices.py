"""Choices for Animes App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class DayChoices(TextChoices):

    MONDAY = "monday", _("Monday")
    TUESDAY = "tuesday", _("Tuesday")
    WEDNESDAY = "wednesday", _("Wednesday")
    THURSDAY = "thursday", _("Thursday")
    FRIDAY = "friday", _("Friday")
    SATURDAY = "saturday", _("Saturday")
    SUNDAY = "sunday", _("Sunday")


class TimezoneChoices(TextChoices):

    JST = "JST", _("Japan Standard Time")
    PST = "PST", _("Pacific Standard Time")
    EST = "EST", _("Eastern Standard Time")
    CST = "CST", _("Central Standard Time")
    GMT = "GMT", _("Greenwich Mean Time")
    CET = "CET", _("Central European Time")

    # TODO: Add more


class StatusChoices(TextChoices):

    FINISHED = "finished", _("Finished")
    AIRING = "airing", _("Airing")
    UPCOMING = "upcoming", _("Upcoming")


class MediaTypeChoices(TextChoices):

    TV = "tv", _("TV")
    OVA = "ova", _("OVA")
    MOVIE = "movie", _("Movie")
    SPECIAL = "special", _("Special")
    ONA = "ona", _("ONA")
    MUSIC = "music", _("Music")


class RatingChoices(TextChoices):

    G = "g", _("G - All Ages")
    PG = "pg", _("PG - Children")
    PG13 = "pg13", _("PG-13 - Teens 13 and Older")
    R = "r", _("R - 17+ (Violence & Profanity)")
    RPLUS = "rplus", _("R+ - Profanity & Mild Nudity")
    RX = "rx", _("RX - Hentai")


class SourceChoices(TextChoices):

    ORIGINAL = "original", _("Original")
    MANGA = "manga", _("Manga")
    NOVEL = "novel", _("Novel")
    LNOVEL = "lnovel", _("Light Novel")
    VNOVEL = "vnovel", _("Visual Novel")
    GAME = "game", _("Game")
    BOOK = "book", _("Book")
    RADIO = "radio", _("Radio")
    MUSIC = "music", _("Music")


class SeasonChoices(TextChoices):

    WINTER = "winter", _("Winter")
    SPRING = "spring", _("Spring")
    SUMMER = "summer", _("Summer")
    FALL = "fall", _("Fall")
