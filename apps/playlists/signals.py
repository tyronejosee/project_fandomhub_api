"""Signals for Playlists App."""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AnimeListItem, MangaListItem


@receiver(post_save, sender=AnimeListItem)
def update_anime_on_favorite(sender, instance, **kwargs):
    """Update anime statistics when a anime is marked as favorite."""
    anime = instance.anime_id

    if instance.is_favorite:
        anime.members += 1
        anime.favorites += 1
        anime.save()
    else:
        anime.members -= 1
        anime.favorites -= 1

    anime.save()


@receiver(post_save, sender=MangaListItem)
def update_manga_on_favorite(sender, instance, **kwargs):
    """Update manga statistics when a manga is marked as favorite."""
    manga = instance.manga_id

    if instance.is_favorite:
        manga.members += 1
        manga.favorites += 1
        manga.save()
    else:
        manga.members -= 1
        manga.favorites -= 1

    manga.save()
