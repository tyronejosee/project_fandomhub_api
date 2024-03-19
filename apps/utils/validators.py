"""Validators for Utils App."""

from django.core.validators import RegexValidator


def validate_name(value):
    """Validate that the input value contains only letters or spaces."""
    validator = RegexValidator(
        regex="^[A-Za-z ]+$",
        message="Name must contain only letters or spaces",
        code="invalid_name"
    )
    validator(value)
