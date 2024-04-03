"""Signals for Playlists App."""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PlaylistAnime


@receiver(post_save, sender=PlaylistAnime)
def update_anime_on_favorite(sender, instance, **kwargs):
    """Update anime statistics when a playlist anime is marked as favorite."""
    if instance.is_favorite:
        anime = instance.anime
        anime.num_list_users += 1
        anime.favorites += 1
        anime.save()
    else:
        anime = instance.anime
        anime.num_list_users -= 1
        anime.favorites -= 1
        anime.save()
