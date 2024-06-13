"""Models for Characters App."""

from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.paths import image_path
from apps.persons.models import Person
from apps.persons.choices import CategoryChoices
from apps.animes.models import Anime
from apps.mangas.models import Manga
from .managers import CharacterManager
from .choices import RoleChoices


class Character(BaseModel, SlugMixin):
    """Model definition for Character."""

    name = models.CharField(_("name"), max_length=255)
    name_kanji = models.CharField(_("name kanji"), max_length=255)
    about = models.TextField(_("about"), blank=True)
    role = models.CharField(_("role"), max_length=15, choices=RoleChoices.choices)
    image = models.ImageField(
        _("image"),
        upload_to=image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "webp"]),
            ImageSizeValidator(max_width=600, max_height=600),
            FileSizeValidator(limit_mb=1),
        ],
    )
    voices = models.ManyToManyField(Person, through="CharacterVoice", blank=True)
    animes = models.ManyToManyField(Anime, through="CharacterAnime", blank=True)
    mangas = models.ManyToManyField(Manga, through="CharacterManga", blank=True)
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    # TODO: Check for possible errors

    objects = CharacterManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character")
        verbose_name_plural = _("characters")

    def __str__(self):
        return str(self.name)


class CharacterVoice(BaseModel):
    """Model definition for CharacterVoice."""

    character_id = models.ForeignKey(
        Character,
        related_name="character_voice",
        limit_choices_to={"is_available": True},
        on_delete=models.CASCADE,
    )
    voice_id = models.ForeignKey(
        Person,
        related_name="character_voice",
        limit_choices_to={
            "category": CategoryChoices.VOICE_ACTOR,
            "is_available": True,
        },
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character voice")
        verbose_name_plural = _("character voices")
        constraints = [
            models.UniqueConstraint(
                fields=["character_id", "voice_id"],
                name="unique_character_voices",
            )
        ]

    def __str__(self):
        return str(f"{self.character_id} - {self.voice_id}")


class CharacterAnime(BaseModel):
    """Model definition for CharacterAnime."""

    character_id = models.ForeignKey(
        Character,
        related_name="character_anime",
        limit_choices_to={"is_available": True},
        on_delete=models.CASCADE,
    )
    anime_id = models.ForeignKey(
        Anime,
        related_name="character_anime",
        limit_choices_to={"is_available": True},
        on_delete=models.CASCADE,
    )
    # TODO: Remove

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character anime")
        verbose_name_plural = _("character animes")
        constraints = [
            UniqueConstraint(
                fields=["character_id", "anime_id"], name="unique_character_anime"
            )
        ]

    def __str__(self):
        return str(f"{self.character_id} - {self.anime_id}")


class CharacterManga(BaseModel):
    """Model definition for CharacterManga."""

    character_id = models.ForeignKey(
        Character,
        related_name="character_manga",
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
    )
    manga_id = models.ForeignKey(
        Manga,
        related_name="character_manga",
        on_delete=models.CASCADE,
        limit_choices_to={"is_available": True},
    )
    # TODO: Remove

    class Meta:
        ordering = ["pk"]
        verbose_name = _("character manga")
        verbose_name_plural = _("character mangas")
        constraints = [
            UniqueConstraint(
                fields=["character_id", "manga_id"], name="unique_character_manga"
            )
        ]

    def __str__(self):
        return str(f"{self.character_id} - {self.manga_id}")
