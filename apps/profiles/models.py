"""Models for Profiles App."""

from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from apps.utils.models import BaseModel
from apps.utils.paths import profile_image_path
from apps.contents.models import Anime


User = settings.AUTH_USER_MODEL


class Profile(BaseModel):
    """Model definition for Profile (Entity)."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    bio = models.TextField(_('Bio'), blank=True, null=True)
    website = models.URLField(_('Website'), blank=True, null=True)
    birth_date = models.DateField(_('Birth Date'), blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to=profile_image_path, blank=True, null=True)
    cover = models.ImageField(_('Cover'), upload_to=profile_image_path, blank=True, null=True)

    class Meta:
        """Meta definition for Profile."""
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return str(self.user.username)


class Follow(BaseModel):
    """Model definition for Follow (Association)."""
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following', verbose_name=_('Follower')
    )
    followed_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers', verbose_name=_('Followed User')
    )

    class Meta:
        """Meta definition for Follow."""
        unique_together = ('follower', 'followed_user')
        verbose_name = _('Follow')
        verbose_name_plural = _('Follows')

    def __str__(self):
        return f"{self.follower.username} follows {self.followed_user.username}"


class AnimeList(models.Model):
    """Model definition for AnimeList (Association)."""
    anime = models.ForeignKey(Anime, related_name='anime_list_status', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_list_status', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    num_episodes_watched = models.IntegerField(default=0)
