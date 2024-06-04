"""Managers for Animes App."""

from django.db.models import Manager


class AnimeManager(Manager):
    """Manager for Anime model."""

    def get_available(self):
        return self.filter(available=True)

    def get_unavailable(self):
        return self.filter(available=False)

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
                "rank",
                "popularity",
                "num_list_users",
            )
        )
