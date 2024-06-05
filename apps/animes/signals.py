"""Signals for Animes App."""

from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Anime, AnimeStats


@receiver(post_save, sender=Anime)
def create_anime_stats(sender, instance, created, **kwargs):
    """Signal creates an instance of stats associated with an anime."""
    if created:
        AnimeStats.objects.create(anime_id=instance)
