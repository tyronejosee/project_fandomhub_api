"""Models for Users App."""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext as _

from .managers import UserManager
from .choices import Role


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email"), max_length=255, unique=True, db_index=True)
    username = models.CharField(_("username"), max_length=255, unique=True)
    first_name = models.CharField(
        _("first name"), max_length=255, blank=True, null=True
    )
    last_name = models.CharField(_("last name"), max_length=255, blank=True, null=True)
    role = models.CharField(
        _("role"), max_length=15, choices=Role.choices, default=Role.MEMBER
    )
    is_active = models.BooleanField(_("is active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["pk"]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return str(self.username)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
