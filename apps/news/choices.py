"""Choices for News App."""

from django.utils.translation import gettext as _


TAG_CHOICES = [
    ("pending", _("Pending")),
    ("new_anime", _("New Anime")),
    ("new_manga", _("New Manga")),
    ("spoiler", _("Spoiler")),
    ("review", _("Review")),
    ("interview", _("Interview")),
    ("event", _("Event")),
    ("recommendation", _("Recommendation")),
]
