"""Signals for Playlists App."""

import logging
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AnimeListItem, MangaListItem


logger = logging.getLogger(__name__)


@receiver(post_save, sender=AnimeListItem)
def update_anime_on_save(sender, instance, created, **kwargs):
    """Signal update stats when user changes their animelist."""
    try:
        with transaction.atomic():
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
            # user_update = instance.updated_at
            # old_instance = AnimeListItem.objects.get(pk=instance.pk)
            # if user_update != old_instance.updated_at:
            #     anime.calculate_score(user_score)

            anime.calculate_score(user_score)
            anime.calculate_ranked()
            anime.calculate_popularity()

            # Update all fields
            anime.save(
                update_fields=[
                    "members",
                    "favorites",
                    "score",
                    "ranked",
                    "popularity",
                ]
            )
    except Exception as e:
        logger.error(f"ANIMELIST ERROR: {e}")


@receiver(post_save, sender=MangaListItem)
def update_manga_on_save(sender, instance, created, **kwargs):
    """Signal update stats when user changes their mangalist."""
    try:
        with transaction.atomic():
            manga = instance.manga_id
            user_score = instance.score

            if created:
                manga.members += 1

            if instance.is_favorite:
                manga.favorites += 1
            else:
                manga.favorites -= 1

            if manga.favorites < 0:
                manga.favorites = 0

            # TODO: Fix so that when the user updates, calculate_score is not executed again
            # user_update = instance.updated_at
            # old_instance = mangaListItem.objects.get(pk=instance.pk)
            # if user_update != old_instance.updated_at:
            #     manga.calculate_score(user_score)

            manga.calculate_score(user_score)
            manga.calculate_ranked()
            manga.calculate_popularity()

            # Update all fields
            manga.save(
                update_fields=[
                    "members",
                    "favorites",
                    "score",
                    "ranked",
                    "popularity",
                ]
            )
    except Exception as e:
        logger.error(f"MANGALIST ERROR: {e}")
