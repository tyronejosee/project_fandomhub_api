"""Managers for Animes App."""

from django.db.models import Q

from apps.utils.managers import BaseManager


class AnimeManager(BaseManager):
    """Manager for Anime model."""

    def get_popular(self):
        return self.get_available().order_by("-popularity")

    def get_recommendations(self):
        return (
            self.get_available()
            .filter(is_recommended=True)
            .order_by("-updated_at")
            .only(
                "id",
                "name",
                "image",
                "episodes",
                "ranked",
                "popularity",
                "members",
            )
        )

    def get_by_genre(self, genre):
        return (
            self.get_available()
            .filter(genres=genre)
            .only(
                "id",
                "name",
                "image",
                "episodes",
                "ranked",
                "popularity",
                "members",
            )
        )  # OPTIMIZE: 44.3 ms

    def get_similar_animes(self, anime):
        return (
            self.filter(
                Q(genres__in=anime.genres.all()) | Q(themes__in=anime.themes.all())
            )
            .exclude(id=anime.id)
            .distinct()[:25]
        )

    def get_by_year_and_season(self, season, year):
        return self.filter(season=season, year=year)

    def get_by_studio(self, studio):
        return self.get_available().filter(studio_id=studio)
