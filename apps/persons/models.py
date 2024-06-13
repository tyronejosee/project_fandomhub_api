"""Models for Persons App."""

from datetime import date
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.validators import FileSizeValidator, ImageSizeValidator
from apps.utils.mixins import SlugMixin
from apps.utils.paths import image_path
from apps.animes.models import Anime
from .managers import PersonManager
from .choices import CategoryChoices, LanguageChoices


class Person(BaseModel, SlugMixin):
    """Model definition for Person."""

    name = models.CharField(_("name"), max_length=255, unique=True)
    given_name = models.CharField(
        _("given name"),
        max_length=255,
        blank=True,
        help_text="first_name",
    )
    family_name = models.CharField(
        _("family name"),
        max_length=255,
        blank=True,
        help_text="last_name",
    )
    image = models.ImageField(
        _("image"),
        upload_to=image_path,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "webp"]),
            ImageSizeValidator(max_width=1080, max_height=1080),
            FileSizeValidator(limit_mb=1),
        ],
    )
    alternate_names = models.JSONField(
        _("alternative names"),
        blank=True,
        null=True,
        default=list,
    )
    birthday = models.DateField(_("birthday"), blank=True, null=True)
    about = models.TextField(_("about"), blank=True, null=True)
    website = models.URLField(_("website"), blank=True, null=True)
    language = models.CharField(
        _("language"),
        max_length=20,
        choices=LanguageChoices.choices,
        default=LanguageChoices.JAPANESE,
    )
    category = models.CharField(
        max_length=20,
        db_index=True,
        choices=CategoryChoices.choices,
        verbose_name=_("category"),
    )
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    objects = PersonManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    def __str__(self):
        return self.name

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.birthday.year
            - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        )


class StaffAnime(BaseModel):
    """Model definition for StaffAnime."""

    person_id = models.ForeignKey(
        Person,
        related_name="person_anime",
        limit_choices_to={"is_available": True},  # TODO: Add type
        on_delete=models.CASCADE,
    )
    anime_id = models.ForeignKey(
        Anime,
        related_name="person_anime",
        limit_choices_to={"is_available": True},
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = _("staff anime")
        verbose_name_plural = _("staff animes")
        constraints = [
            UniqueConstraint(
                fields=["person_id", "anime_id"], name="unique_staff_anime"
            )
        ]

    def __str__(self):
        return str(f"{self.person_id} - {self.anime_id}")
