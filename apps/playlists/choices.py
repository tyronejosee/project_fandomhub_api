"""Choices for Playlists App."""

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class StatusChoices(TextChoices):  # TODO: AnimeStatus

    PENDING = "pending", _("Pending")  # TODO: Remove
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
