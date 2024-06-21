"""Filters for Producers App."""

from django.db.models import TextChoices
from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Producer


class ProducerFilter(BaseFilter):
    """Filter for Producer model."""

    class OrderByChoices(TextChoices):

        ID = "id", _("UUID")
        NAME = "name", _("Name")
        ESTABLISHED = "established", _("Established")
        FAVORITES = "favorites", _("Favorites")

    order_by = filters.ChoiceFilter(
        choices=OrderByChoices.choices,
        method="filter_order_by",
        label=_("Available Producer order_by properties"),
    )

    class Meta:
        model = Producer
        fields = [
            "order_by",
            "sort",
            "letter",
        ]

    def filter_order_by(self, queryset, name, value):
        return queryset.order_by(value)
