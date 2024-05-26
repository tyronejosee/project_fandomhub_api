"""Choices for Playlists App."""

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class StatusChoices(TextChoices):

    PENDING = "pending", _("Pending")
    WATCHING = "watching", _("Watching")
    COMPLETED = "completed", _("Completed")
    ON_HOLD = "on_hold", _("On Hold")
    DROPPED = "dropped", _("Dropped")
    PLAN_WATCH = "plan_watch", _("Plan to Watch")
