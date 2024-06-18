"""Filters for Persons App."""

from django_filters import rest_framework as filters

from .models import Person


class PersonFilter(filters.FilterSet):
    """Filter for Person model."""

    sort = filters.ChoiceFilter(
        label="Sort",
        choices=[("asc", "Ascending"), ("desc", "Descending")],
        method="filter_by_order",
    )
    letter = filters.CharFilter(field_name="name", method="filter_letter")

    class Meta:
        model = Person
        fields = ["sort"]

    def filter_letter(self, queryset, name, value):
        return queryset.filter(name__istartswith=value)

    def filter_by_order(self, queryset, name, value):
        if value == "asc":
            return queryset.order_by("name")
        elif value == "desc":
            return queryset.order_by("-name")
        return queryset
