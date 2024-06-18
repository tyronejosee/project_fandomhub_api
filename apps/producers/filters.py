"""Filters for Producers App."""

from apps.utils.filters import BaseFilter
from .models import Producer


class ProducerFilter(BaseFilter):
    """Filter for Producer model."""

    class Meta:
        model = Producer
        fields = ["sort", "letter"]
