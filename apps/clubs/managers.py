"""Manager for Clubs App."""

from django.db.models import Manager


class ClubManager(Manager):
    """Manager for Club model."""

    def get_available(self):
        return self.filter(available=True)
