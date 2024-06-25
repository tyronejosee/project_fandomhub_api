"""Signals for Playlists App."""

import logging
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AnimeListItem, MangaListItem


logger = logging.getLogger(__name__)


@receiver(post_save, sender=AnimeListItem)
def update_anime_on_save(sender, instance, created, **kwargs):
    """Signal update statistics when a user updates their animelist."""

    def update_statistics():
        try:
            anime = instance.anime_id
            user_score = instance.score

            if created:
                anime.members += 1

            if instance.is_favorite:
                anime.favorites += 1
            else:
                anime.favorites -= 1

            if anime.favorites < 0:
                anime.favorites = 0

            # TODO: Fix so that when the user updates, calculate_score is not executed again
            anime.calculate_score(user_score)
            anime.calculate_ranked()
            anime.calculate_popularity()

            # Update all fields
            anime.save(
                update_fields=["members", "favorites", "score", "ranked", "popularity"]
            )
        except Exception as e:
            logger.error(f"ANIMELIST ERROR: {e}")

    transaction.on_commit(update_statistics)


@receiver(post_save, sender=MangaListItem)
def update_manga_on_save(sender, instance, **kwargs):
    """Signal update statistics when a user updates their mangalist."""
    manga = instance.manga_id

    if instance.is_favorite:
        manga.members += 1
        manga.favorites += 1
        manga.save()
    else:
        manga.members -= 1
        manga.favorites -= 1

    manga.save()
