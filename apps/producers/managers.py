"""Managers for Producers App."""

from django.db.models import Manager


class ProducerManager(Manager):
    """Manager for Producer model."""

    def get_available(self):
        return self.filter(is_available=True)
