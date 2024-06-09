"""Choices for Playlists App."""

from django.db.models import TextChoices, IntegerChoices
from django.utils.translation import gettext_lazy as _


class ScoreChoices(IntegerChoices):

    ONE = 1, _("1 - Appaling")
    TWO = 2, _("2 - Horrible")
    THREE = 3, _("3 - Very Bad")
    FOUR = 4, _("4 - Bad")
    FIVE = 5, _("5 - Average")
    SIX = 6, _("6 - Fine")
    SEVEN = 7, _("7 - Good")
    EIGHT = 8, _("8 - Very Good")
    NINE = 9, _("9 - Great")
    TEN = 10, _("10 - Masterpiece")


class PriorityChoices(TextChoices):

    LOW = "low", _("Low")
    MEDIUM = "medium", _("Medium")
    HIGH = "high", _("High")


class StorageChoices(TextChoices):

    DVD = "dvd", _("DVD")
    BLURAY = "bluray", _("Blu-ray")
    STREAMING = "streaming", _("Streaming")
    DOWNLOAD = "download", _("Download")


class AnimeStatusChoices(TextChoices):

    WATCHING = "watching", _("Watching")
    COMPLETED = "completed", _("Completed")
    ON_HOLD = "on_hold", _("On Hold")
    DROPPED = "dropped", _("Dropped")
    PLAN_WATCH = "plan_watch", _("Plan to Watch")


class MangaStatusChoices(TextChoices):

    READING = "reading", _("Reading")
    COMPLETED = "completed", _("Completed")
    ON_HOLD = "on_hold", _("On Hold")
    DROPPED = "dropped", _("Dropped")
    PLAN_READ = "plan_read", _("Plan to Read")
