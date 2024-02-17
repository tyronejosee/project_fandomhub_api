"""Models for Users App."""

import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext as _
from django.utils import timezone
from apps.profiles.models import Profile


class UserManager(BaseUserManager):
    """Manages User instances."""

    def create_user(self, email, password=None, **kwargs):
        """Creates and returns a user with the given email and password."""
        if not email:
            raise ValueError(_('Users must have an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)

        user.set_password(password)
        user.save()

        profile = Profile.objects.create(user=user)
        profile.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        """Creates a superuser with the given email and password."""
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        user = self.create_user(email, password=password, **kwargs)
        return user


class Role(models.Model):
    """Model definition for Role (Association)."""
    name = models.CharField(_('Name'), max_length=50, unique=True)
    permissions = models.ManyToManyField(
        'auth.Permission', blank=True, verbose_name=_('Permissions')
    )

    class Meta:
        """Meta definition for Role model."""
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return str(self.name)


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User (Entity)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('Email'), max_length=255, unique=True,)
    username = models.CharField(_('Username'), max_length=255, unique=True)
    first_name = models.CharField(
        _('First Name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(
        _('Last Name'), max_length=255, blank=True, null=True)
    roles = models.ManyToManyField(
        Role, related_name='users', blank=True, verbose_name=_('Roles'))
    is_active = models.BooleanField(_('Is Active'), default=True)
    is_staff = models.BooleanField(_('Is Staff'), default=False)
    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        """Meta definition for User model."""
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return str(self.username)
