"""Filter for Characters App."""

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from apps.utils.filters import BaseFilter
from .models import Character
from .choices import RoleChoices, OrderByChoices


class CharacterFilter(BaseFilter):
    """Filter for Character model."""

    order_by = filters.ChoiceFilter(
        choices=OrderByChoices.choices,
        method="filter_order_by",
        label=_("Available Character order_by properties"),
    )
    role = filters.ChoiceFilter(
        choices=RoleChoices.choices,
        label=_("Available sorting properties by character role"),
    )

    def filter_order_by(self, queryset, name, value):
        return queryset.order_by(value)

    class Meta:
        model = Character
        fields = [
            "order_by",
            "role",
            "sort",
            "letter",
        ]
