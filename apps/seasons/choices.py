"""Choices for Seasons App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class SeasonChoices(TextChoices):

    WINTER = "winter", _("Winter")
    SPRING = "spring", _("Spring")
    SUMMER = "summer", _("Summer")
    FALL = "fall", _("Fall")
