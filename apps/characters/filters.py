"""Filter for Characters App."""

from django_filters import rest_framework as filters

from .models import Character
from .choices import RoleChoices


class CharacterFilter(filters.FilterSet):
    """Filter for Character model."""

    role = filters.ChoiceFilter(choices=RoleChoices.choices)

    class Meta:
        model = Character
        fields = [
            "role",
        ]
