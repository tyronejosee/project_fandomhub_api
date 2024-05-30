"""Signals for Utilities App."""

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver


@receiver(post_delete)
def remove_image_on_delete(sender, instance, **kwargs):
    """Signal removes the related image when the instance is deleted."""
    if hasattr(instance, "image") and instance.image:
        if instance.image.path and os.path.exists(instance.image.path):
            os.remove(instance.image.path)


# TODO: Add signal connections for the models in the anime and manga app
