"""Models for Seasons App."""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from apps.utils.models import BaseModel
from .managers import SeasonManager
from .choices import SeasonChoices


class Season(BaseModel):
    """Model definition for Season."""

    season = models.CharField(
        _("season"),
        max_length=10,
        choices=SeasonChoices.choices,
        default=SeasonChoices.PENDING,
    )
    year = models.IntegerField(
        _("year"),
        default=2010,
        db_index=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2100)],
    )
    fullname = models.CharField(_("fullname"), max_length=255, unique=True, blank=True)

    objects = SeasonManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = _("season")
        verbose_name_plural = _("season")

    def __str__(self):
        return str(self.fullname)

    def save(self, *args, **kwargs):
        # Override the save method to update the fullname field
        fullname_caps = self.season.capitalize()
        self.fullname = f"{fullname_caps} {self.year}"
        if Season.objects.filter(fullname=self.fullname).exists():
            raise ValidationError(_("The fullname field must be unique."))
        super().save(*args, **kwargs)
