"""Managers for News App."""

from apps.utils.managers import BaseManager


class NewsManager(BaseManager):
    """Manager for News model."""

    def get_anime_news(self, anime):
        return (
            self.get_available()
            .filter(anime_relations=anime)
            .order_by("-created_at")[:25]
        )

    def get_manga_news(self, manga):
        return (
            self.get_available()
            .filter(manga_relations=manga)
            .order_by("-created_at")[:25]
        )
