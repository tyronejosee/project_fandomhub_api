"""Choices for Categories App."""

from django.utils.translation import gettext as _


TAG_CHOICES = [
    (0, _("Pending")),
    (1, _("Official Site")),
    (2, _("Crunchyroll")),
    (3, _("Netflix")),
    (4, _("Youtube Acccount")),
    (5, _("X Account")),
]

SEASON_CHOICES = [
    (0, _("Pending")),
    (1, _("Winter")),
    (2, _("Spring")),
    (3, _("Summer")),
    (4, _("Fall")),
]
