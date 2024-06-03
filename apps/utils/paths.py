"""Paths for Utils App."""

from django.utils.text import slugify


def image_path(instance, filename):
    """Generates storage path for associated model images."""
    appname = instance.__class__.__module__.split(".")[1]
    modelname = instance.__class__.__name__.lower()
    extension = filename.split(".")[-1]
    filename = f"{instance.slug}.{extension}"
    return f"{appname}/{modelname}/{filename}"


def profile_image_path(instance, filename):
    """Generates storage path for profile image associated."""
    appname = instance.__class__.__module__.split(".")[1]
    username = instance.user.username
    extension = filename.split(".")[-1]
    filename = f"{username}.{extension}"
    return f"{appname}/{filename}"


def picture_image_path(instance, filename):
    """Generates storage path for associated model Picture model images."""
    appname = instance.__class__.__module__.split(".")[1]
    modelname = instance.__class__.__name__.lower()
    extension = filename.split(".")[-1]
    name = slugify(instance.name)
    filename = f"{name}.{extension}"
    return f"{appname}/{modelname}/{filename}"
