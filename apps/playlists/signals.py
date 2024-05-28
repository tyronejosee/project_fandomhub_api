"""Signals for Playlists App."""

# TODO: Refactor
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import PlaylistAnime, PlaylistManga


# @receiver(post_save, sender=PlaylistAnime)
# def update_anime_on_favorite(sender, instance, **kwargs):
#     """Update anime statistics when a playlist anime is marked as favorite."""
#     if instance.is_favorite:
#         anime = instance.anime
#         anime.num_list_users += 1
#         anime.favorites += 1
#         anime.save()
#     else:
#         anime = instance.anime
#         anime.num_list_users -= 1
#         anime.favorites -= 1
#         anime.save()


# @receiver(post_save, sender=PlaylistManga)
# def update_manga_on_favorite(sender, instance, **kwargs):
#     """Update manga statistics when a playlist manga is marked as favorite."""
#     if instance.is_favorite:
#         manga = instance.manga
#         manga.num_list_users += 1
#         manga.favorites += 1
#         manga.save()
#     else:
#         manga = instance.manga
#         manga.num_list_users -= 1
#         manga.favorites -= 1
#         manga.save()
