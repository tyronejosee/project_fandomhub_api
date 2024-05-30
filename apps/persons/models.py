"""Models for Persons App."""

from django.db import models
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from apps.utils.mixins import SlugMixin
from .managers import PersonManager
from .choices import CategoryChoices


class Person(BaseModel, SlugMixin):
    """Model definition for Person."""

    name = models.CharField(_("name"), max_length=255, unique=True)
    given_name = models.CharField(
        _("given name"),
        max_length=255,
        help_text="first_name",
    )
    family_name = models.CharField(
        _("family name"),
        max_length=255,
        help_text="last_name",
    )
    alternate_names = models.JSONField(_("alternative names"), default=list)
    birthday = models.DateField(_("birthday"), blank=True, null=True)
    about = models.TextField(_("about"), blank=True, null=True)
    website = models.URLField(_("website"), blank=True, null=True)
    category = models.CharField(
        max_length=20,
        db_index=True,
        choices=CategoryChoices.choices,
        verbose_name=_("category"),
    )
    favorites = models.PositiveIntegerField(_("favorites"), default=0)

    # anime = models.JSONField(default=list)
    # manga = models.JSONField(default=list)
    # voices = models.JSONField(default=list)

    objects = PersonManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("person")
        verbose_name_plural = _("persons")

    def __str__(self):
        return self.name
