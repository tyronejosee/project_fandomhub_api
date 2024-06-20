"""Choices for Characters App."""

from django.db.models import TextChoices

from django.utils.translation import gettext as _


class RoleChoices(TextChoices):

    MAIN = "main", _("Main")
    SUPPORTING = "supporting", _("Supporting")


# Filters


class OrderByChoices(TextChoices):

    ID = "id", _("UUID")
    NAME = "name", _("Name")
    FAVORITES = "favorites", _("Favorites")
