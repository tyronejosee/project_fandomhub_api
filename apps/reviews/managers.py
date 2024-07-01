"""Managers for Reviews App."""

from apps.utils.managers import BaseManager


class ReviewManager(BaseManager):
    """Manager for Review model."""

    def get_reviews_for_anime(self, anime):
        return self.get_available().filter(anime=anime).order_by("-created_at")
