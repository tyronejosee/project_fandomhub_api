from django.apps import AppConfig


class MangasConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.mangas"

    def ready(self):
        import apps.mangas.signals
