"""Choices for Producers App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _


class TypeChoices(TextChoices):

    STUDIO = "studio", _("Studio")
    LICENSOR = "licensor", _("Licensor")
    PUBLISHER = "publisher", _("Publisher")
    DISTRIBUTOR = "distributor", _("Distributor")
    NETWORK = "network", _("Network")
    SPONSOR = "sponsor", _("Sponsor")
    PLATFORM = "platform", _("Platform")


class OrderByChoices(TextChoices):

    ID = "id", _("UUID")
    NAME = "name", _("Name")
    ESTABLISHED = "established", _("Established")
    FAVORITES = "favorites", _("Favorites")
