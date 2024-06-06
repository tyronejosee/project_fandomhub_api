"""Choices for Mangas App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class StatusChoices(TextChoices):

    FINISHED = "finished", _("Finished")
    AIRING = "airing", _("Airing")
    UPCOMING = "upcoming", _("Upcoming")


class MediaTypeChoices(TextChoices):

    MANGA = "manga", _("Manga")
    NOVEL = "novel", _("Novel")
    ONESHOT = "oneshot", _("One Shot")
    DOUJINSHI = "doujinshi", _("Doujinshi")
    MANHWA = "manhwa", _("Manhwa")
    OEL = "oel", _("OEL")
