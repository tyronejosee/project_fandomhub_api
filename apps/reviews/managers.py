"""Managers for Reviews App."""

from django.db.models import Manager


class ReviewAnimeManager(Manager):
    """Manager for ReviewAnime model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available anime reviews."""
        return self.get_queryset().filter(available=True)

    def get_reviews_for_anime(self, anime):
        """Get all reviews for a specific anime, ordered by creation date."""
        return self.get_available().filter(anime=anime).order_by("-created_at")


class ReviewMangaManager(Manager):
    """Manager for ReviewManga model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available manga reviews."""
        return self.get_queryset().filter(available=True)

    def get_reviews_for_manga(self, manga):
        """Get all reviews for a specific manga, ordered by creation date."""
        return self.get_available().filter(manga=manga).order_by("-created_at")
