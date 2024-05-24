"""Managers for Reviews App."""

from django.db.models import Manager


class ReviewAnimeManager(Manager):
    """Manager for ReviewAnime model."""

    def get_available(self):
        return self.filter(available=True)

    def get_reviews_for_anime(self, anime):
        return self.get_available().filter(anime=anime).order_by("-created_at")


class ReviewMangaManager(Manager):
    """Manager for ReviewManga model."""

    def get_available(self):
        return self.filter(available=True)

    def get_reviews_for_manga(self, manga):
        return self.get_available().filter(manga=manga).order_by("-created_at")
