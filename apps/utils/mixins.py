"""Mixins for Utils App."""

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

class SlugMixin(models.Model):
    """Mixin providing slug functionality for models."""
    slug = models.SlugField(_('Slug'), unique=True, blank=True, null=True)

    def generate_slug(self, field_name='name'):
        """Generate a slug based on the content of the instance."""
        content = getattr(self, field_name)
        self.slug = slugify(content)

    def save(self, *args, **kwargs):
        if not self.slug or self.slug != self.name:
            self.generate_slug()
        super().save(*args, **kwargs)

    class Meta:
        """Meta definition for SlugMixin."""
        abstract = True
