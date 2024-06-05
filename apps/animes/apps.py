from django.apps import AppConfig


class AnimesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.animes"

    def ready(self):
        import apps.animes.signals
