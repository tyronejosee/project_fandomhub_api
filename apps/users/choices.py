"""Choices for Contents App."""

from django.utils.translation import gettext as _


STATUS_CHOICES = [
    ("client", _("Client")),
    ("admin", _("Admin")),
    ("moderator", _("Moderator")),
    ("helper", _("Helper")),
    ("editor", _("Editor"))
]
