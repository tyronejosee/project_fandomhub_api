"""Choices for News App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class TagChoices(TextChoices):

    PENDING = "pending", _("Pending")
    NEW_ANIME = "new_anime", _("New Anime")
    NEW_MANGA = "new_manga", _("New Manga")
    SPOILER = "spoiler", _("Spoiler")
    REVIEW = "review", _("Review")
    INTERVIEW = "interview", _("Interview")
    EVENT = "event", _("Event")
    RECOMMENDATION = "recommendation", _("Recommendation")
