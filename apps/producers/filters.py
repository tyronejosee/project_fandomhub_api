"""Filters for Producers App."""

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Producer
from .choices import OrderByChoices


class ProducerFilter(BaseFilter):
    """Filter for Producer model."""

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
