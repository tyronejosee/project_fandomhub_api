"""Filters for News App."""

from django.utils.translation import gettext as _
from django_filters import rest_framework as filters

from .models import News
from .choices import TagChoices


class NewsFilter(filters.FilterSet):
    """Filter for News model."""

    tag = filters.ChoiceFilter(
        choices=TagChoices.choices,
        label=_("Available News tags"),
    )

    class Meta:
        model = News
        fields = [
            "tag",
        ]
