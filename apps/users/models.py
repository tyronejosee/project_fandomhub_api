"""Models for Users App."""

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """Manages User instances, including superusers."""

    def _create_user(self, username, email, first_name, last_name, password, is_staff, is_superuser, **extra_fields):
        """Create and return a regular user with an email and password."""
        user = self.model(
            username = username,
            email = email,
            first_name = first_name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, first_name, last_name, password=None, **extra_fields):
        """Create a standard user."""
        return self._create_user(username, email, first_name, last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, first_name, last_name, password=None, **extra_fields):
        """Create a superuser."""
        return self._create_user(username, email, first_name, last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """Entity type model for User."""
    username = models.CharField(_('Username'), max_length = 255, unique = True)
    email = models.EmailField(_('Email'),max_length=255, unique=True,)
    first_name = models.CharField(_('First Name'), max_length = 255, blank = True, null=True)
    last_name = models.CharField(_('Last Name'), max_length = 255, blank = True, null=True)
    image = models.ImageField(_('Image'), upload_to='users/', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(_('Is Active'), default = True)
    is_staff = models.BooleanField(_('Is Staff'), default = False)
    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    class Meta:
        """Meta definition for User model."""
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
