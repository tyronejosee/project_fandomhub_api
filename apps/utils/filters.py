"""Filters for Utils App."""

from rest_framework.exceptions import NotFound
from django_filters import rest_framework as filters


class BaseFilter(filters.FilterSet):
    """Base filter class with common filters."""

    sort = filters.ChoiceFilter(
        label="Sort",
        choices=[("asc", "Ascending"), ("desc", "Descending")],
        method="filter_by_order",
    )
    letter = filters.CharFilter(field_name="name", method="filter_letter")

    def filter_letter(self, queryset, name, value):
        filtered_queryset = queryset.filter(name__istartswith=value)
        print(filtered_queryset)
        if not filtered_queryset.exists():
            raise NotFound("No data found for this letter.")
        return filtered_queryset

    def filter_by_order(self, queryset, name, value):
        if value == "asc":
            return queryset.order_by("name")
        elif value == "desc":
            return queryset.order_by("-name")
        return queryset
