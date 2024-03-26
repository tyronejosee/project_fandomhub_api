"""Mixins for Utils App."""

from django.db import models
from django.http import Http404
from django.core.cache import cache
from django.utils.text import slugify
from django.utils.translation import gettext as _
from rest_framework.response import Response
from rest_framework import status


class SlugMixin(models.Model):
    """Mixin providing slug functionality for models."""
    slug = models.SlugField(_("Slug"), unique=True, blank=True, null=True)

    def generate_slug(self, field_name="name"):
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


class LogicalDeleteMixin:
    """Mixin for logical deletion of instances."""

    def destroy(self, request, *args, **kwargs):
        """Deletes the instance logically by marking it as unavailable."""
        try:
            instance = self.get_object()
            instance.available = False
            instance.save()
            cache.clear()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(
                {"errors": _("Resource not found.")},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
