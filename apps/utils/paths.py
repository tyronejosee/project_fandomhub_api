"""Paths for Utils App."""


def image_path(instance, filename):
    """Generates storage path for associated model images."""
    # appname = apps.contents.models
    appname = instance.__class__.__module__.split(".")[1]
    modelname = instance.__class__.__name__.lower()
    extension = filename.split(".")[-1]
    filename = f"{instance.slug}.{extension}"
    return f"{appname}/{modelname}/{filename}"


def profile_image_path(instance, filename):
    """Generates storage path for profile image associated."""
    # appname = apps.contents.models
    appname = instance.__class__.__module__.split(".")[1]
    username = instance.user.username
    extension = filename.split(".")[-1]
    filename = f"{username}.{extension}"
    return f"{appname}/{filename}"
