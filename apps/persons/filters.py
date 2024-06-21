"""Filters for Persons App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Person


class PersonFilter(BaseFilter):
    """Filter for Person model."""

    class OrderByChoices(TextChoices):

        ID = "id", _("UUID")
        NAME = "name", _("Name")
        BIRTHDAY = "birthday", _("Birthday")
        FAVORITES = "favorites", _("Favorites")

    order_by = filters.ChoiceFilter(
        choices=OrderByChoices.choices,
        method="filter_order_by",
        label=_("Available Person order_by properties"),
    )

    class Meta:
        model = Person
        fields = [
            "order_by",
            "sort",
            "letter",
        ]
