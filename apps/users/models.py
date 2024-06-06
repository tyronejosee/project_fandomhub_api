"""Models for Users App."""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _

from .managers import UserManager
from .choices import RoleChoices


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email"), max_length=255, unique=True, db_index=True)
    username = models.CharField(_("username"), max_length=255, unique=True)
    role = models.CharField(
        _("role"),
        max_length=15,
        choices=RoleChoices.choices,
        default=RoleChoices.MEMBER,
    )
    is_online = models.BooleanField(_("is online"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["pk"]
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return str(self.username)
