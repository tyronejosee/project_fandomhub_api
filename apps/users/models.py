"""Models for Users App."""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext as _

from .managers import UserManager


class Role(models.Model):
    """Model definition for Role (Association)."""
    name = models.CharField(
        _("name"), max_length=50, unique=True, db_index=True)
    permissions = models.ManyToManyField(
        "auth.Permission", blank=True, verbose_name=_("permissions"))

    class Meta:
        ordering = ["pk"]
        verbose_name = _("role")
        verbose_name_plural = _("roles")

    def __str__(self):
        return str(self.name)


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User (Entity)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        _("email"), max_length=255, unique=True, db_index=True)
    username = models.CharField(
        _("username"), max_length=255, unique=True, db_index=True)
    first_name = models.CharField(
        _("first name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(
        _("last name"), max_length=255, blank=True, null=True)
    roles = models.ManyToManyField(
        Role, related_name="users", blank=True, verbose_name=_("roles"))
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
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}"
