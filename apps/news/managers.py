"""Managers for News App."""

from django.db.models import Manager


class NewsManager(Manager):
    """Manager for News model."""

    def get_available(self):
        return self.filter(available=True)

    def get_anime_news(self, anime):
        return (
            self.get_available()
            .filter(anime_relations=anime)
            .order_by("-created_at")[:25]
        )
