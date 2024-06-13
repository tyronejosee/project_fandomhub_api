"""Signals for Utilities App."""

import os
from PIL import Image
from io import BytesIO
import logging
from django.db.models.signals import post_delete, pre_save
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.dispatch import receiver

from apps.animes.models import Anime
from apps.mangas.models import Manga


logger = logging.getLogger(__name__)


@receiver(post_delete)
def remove_image_on_delete(sender, instance, **kwargs):
    """Signal removes the related image when the instance is deleted."""
    if hasattr(instance, "image") and instance.image:
        if instance.image.path and os.path.exists(instance.image.path):
            os.remove(instance.image.path)


@receiver(pre_save, sender=Anime)
@receiver(pre_save, sender=Manga)
def set_imagen(sender, instance, **kwargs):
    """Signal to reduce image quality to 70% and save in webp format."""
    if not instance.image:
        return

    try:
        image = Image.open(instance.image)

        if image.width < 500 or image.height < 500:
            logger.warning(f"Low image quality: {instance.name}'s image")

        # Compress to 70% quality
        output = BytesIO()
        image.save(output, format="JPEG", quality=70)
        output.seek(0)
        instance.image = InMemoryUploadedFile(
            output,
            "ImageField",
            "%s.jpg" % instance.image.name.split(".")[0],
            "image/jpeg",
            output.tell(),
            None,
        )

        # Save a WEBP version if it doesn't have the corresponding extension
        if not instance.image.name.lower().endswith(".webp"):
            output_webp = BytesIO()
            image.save(output_webp, format="WEBP", quality=70)
            output_webp.seek(0)
            instance.image = InMemoryUploadedFile(
                output_webp,
                "ImageField",
                "%s.webp" % instance.image.name.split(".")[0],
                "image/webp",
                output_webp.tell(),
                None,
            )
    except Exception as e:
        logger.error(f"Error processing image: {e}")
