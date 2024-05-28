"""Validators for Utils App."""

from PIL import Image
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_name(value):
    """Validate that the input value contains only letters or spaces."""
    validator = RegexValidator(
        regex="^[A-Za-z ]+$",
        message="Name must contain only letters or spaces",
        code="invalid_name",
    )
    validator(value)


@deconstructible
class ImageSizeValidator:
    """Validator to ensure the image does not exceed a specified size."""

    message = _("The image must have a maximum size of %(max_width)sx%(max_height)spx")
    code = "invalid_max_size"

    def __init__(self, max_width, max_height):
        if not isinstance(max_width, int) or not isinstance(max_height, int):
            raise TypeError("max_width and max_height must be integers")
        self.max_width = max_width
        self.max_height = max_height

    def __call__(self, image):
        img = Image.open(image)
        width, height = img.size
        if width > self.max_width or height > self.max_height:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "max_width": self.max_width,
                    "max_height": self.max_width,
                },
            )


@deconstructible
class FileSizeValidator:
    """Validator to check if a file's size exceeds a given limit."""

    message = _("File size must be under %(limit)s. Current size is %(size)s.")
    code = "invalid_size"

    def __init__(self, limit_mb, message=None, code=None):
        self.limit = limit_mb * 1024 * 1024

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if value.size > self.limit:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "limit": filesizeformat(self.limit),
                    "size": filesizeformat(value.size),
                },
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.limit == other.limit
            and self.message == other.message
            and self.code == other.code
        )
