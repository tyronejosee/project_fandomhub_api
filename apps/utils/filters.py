"""Filters for Utils App."""

from rest_framework.exceptions import NotFound
from django_filters import rest_framework as filters

from .choices import SortChoices


class BaseFilter(filters.FilterSet):
    """Base filter class with common filters."""

    sort = filters.ChoiceFilter(
        choices=SortChoices.choices,
        method="filter_by_order",
        label="Search query sort direction",
    )
    letter = filters.CharFilter(
        field_name="name",
        method="filter_by_letter",
        label="Return entries starting with the given letter",
    )

    def filter_by_letter(self, queryset, name, value):
        filtered_queryset = queryset.filter(name__istartswith=value)

        if not filtered_queryset.exists():
            raise NotFound("No data found for this letter.")
        return filtered_queryset

    def filter_by_order(self, queryset, name, value):
        order_by = self.data.get("order_by", "name")
        if value == "asc":
            return queryset.order_by(order_by)
        elif value == "desc":
            return queryset.order_by("-" + order_by)
        return queryset
