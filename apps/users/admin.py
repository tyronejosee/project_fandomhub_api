"""Admin for Users App."""

from django.contrib import admin
from django.utils.translation import gettext as _

from .models import User, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    """Admin config for Role model."""
    list_display = ["name",]
    list_display_links = ["name"]
    search_fields = ["name",]
    list_filter = ["name",]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["name",]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin config for User model."""
    list_display = ["username", "email", "is_staff", "is_superuser"]
    list_display_links = ["username"]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["username",]

    fieldsets = [
        (
            _("Account info"),
            {
                "fields": ["pk", "username", "email", "password", "is_active"]
            }
        ),
        (
            _("Personal info"),
            {
                "fields": ["first_name", "last_name"]
            }
        ),
        (
            _("Permissions"),
            {
                "fields": ["is_staff", "is_superuser", "roles",]
            }
        ),
        (
            _("Records"),
            {
                "fields": ["last_login", "date_joined"]
            }
        ),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide",],
                "fields": [
                    "username", "email", "first_name", "last_name",
                    "password1", "password2", "is_staff", "is_superuser"
                ],
            }
        ),
    ]
