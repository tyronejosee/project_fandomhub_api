"""Managers for Contents App."""

from django.db.models import Manager


class AnimeManager(Manager):
    """Manager for Anime model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available animes"""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Get all unavailable animes"""
        return self.get_queryset().filter(available=False)

    def get_popular(self):
        """Get all the most popular anime"""
        return self.get_available().order_by("-popularity")


class MangaManager(Manager):
    """Manager for Manga model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available mangas"""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Get all unavailable mangas"""
        return self.get_queryset().filter(available=False)

    def get_popular(self):
        """Get all the most popular manga"""
        return self.get_available().order_by("-popularity")
