"""Signals for Mangas App."""

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Manga, MangaStats


@receiver(post_save, sender=Manga)
def create_manga_stats(sender, instance, created, **kwargs):
    """Signal creates an instance of stats associated with an manga."""
    if created:
        MangaStats.objects.create(manga_id=instance)
