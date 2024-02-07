"""Admin for Users App."""

from django.contrib import admin
from django.utils.translation import gettext as _
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin config for User model."""
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'date_joined')
    list_display_links = ['username']
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_per_page = 25
    readonly_fields = ('pk',)
    ordering = ('username',)

    fieldsets = (
        (_('Account info'), {'fields': ('pk', 'username', 'email', 'password', 'is_active')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Records'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name', 'password1',
                'password2', 'is_staff', 'is_superuser'
            ),
        }),
    )
