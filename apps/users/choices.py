"""Choices for Users App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class RoleChoices(TextChoices):

    MEMBER = "member", _("Member")
    PREMIUM = "premium", _("Premium")
    CONTRIBUTOR = "contributor", _("Contributor")
    MODERATOR = "moderator", _("Moderator")
    ADMINISTRATOR = "administrator", _("Administrator")
