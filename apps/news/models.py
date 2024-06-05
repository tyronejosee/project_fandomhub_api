"""Models for News App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.paths import image_path
from apps.animes.models import Anime
from apps.mangas.models import Manga
from .managers import NewsManager
from .choices import TagChoices

User = settings.AUTH_USER_MODEL


class News(BaseModel):
    """Model definition for News."""

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    title = models.CharField(_("title"), max_length=100)
    description = models.CharField(_("description"), max_length=255)
    content = models.TextField(_("content"))
    image = models.ImageField(_("image"), upload_to=image_path)
    source = models.URLField(_("source"), max_length=255)
    tag = models.CharField(
        _("tag"),
        max_length=15,
        choices=TagChoices.choices,
        default=TagChoices.PENDING,
    )
    anime_relations = models.ManyToManyField(Anime, blank=True)
    manga_relations = models.ManyToManyField(Manga, blank=True)

    objects = NewsManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("news")
        verbose_name_plural = _("news")
        indexes = [
            models.Index(fields=["title"], name="title_idx"),
            models.Index(fields=["tag"], name="tag_idx"),
        ]

    def __str__(self):
        return str(self.title)
