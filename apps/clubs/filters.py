"""Filters for Clubs App."""

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from .models import Club
from .choices import CategoryChoices


class ClubFilter(filters.FilterSet):
    """Filter for Club model."""

    category = filters.ChoiceFilter(
        field_name="category",
        choices=CategoryChoices.choices,
        label="Available club categories, ex `/?category=companies`",
    )
    public = filters.BooleanFilter(
        field_name="is_public",
        initial=True,
        method="filter_public",
        label=_("Filter all public clubs by default to True, ex `/?public=true`"),
    )

    def filter_public(self, queryset, name, value):
        if value:
            return queryset
        else:
            return queryset.filter(is_public=False)

    class Meta:
        model = Club
        fields = [
            "category",
            "public",
        ]
