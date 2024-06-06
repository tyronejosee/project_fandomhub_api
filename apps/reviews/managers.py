"""Managers for Reviews App."""

from django.db.models import Manager


class ReviewManager(Manager):
    """Manager for Review model."""

    def get_available(self):
        return self.filter(is_available=True)

    def get_reviews_for_anime(self, anime):
        return self.get_available().filter(anime=anime).order_by("-created_at")
