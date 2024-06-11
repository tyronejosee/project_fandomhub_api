"""Admin for Clubs App."""

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.utils.admin import BaseAdmin
from .models import Club, ClubMember, Event, Topic, Discussion
from .resources import (
    ClubResource,
    ClubMemberResource,
    EventResource,
    TopicResource,
    DiscussionResource,
)


@admin.register(Club)
class ClubAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Club model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["name", "members", "is_public", "is_available"]
    list_filter = ["is_available", "is_public", "category"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    resource_class = ClubResource


@admin.register(ClubMember)
class ClubMemberAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for ClubMember model."""

    ordering = ["-created_at"]
    search_fields = ["club_id", "user_id"]
    list_display = ["club_id", "user_id", "is_available"]
    list_filter = ["is_available", "club_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = ClubMemberResource


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Event model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["club_id", "name", "is_available"]
    list_filter = ["is_available", "club_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = EventResource


@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Topic model."""

    ordering = ["-created_at"]
    search_fields = ["name"]
    list_display = ["club_id", "is_available"]
    list_filter = ["is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = TopicResource


@admin.register(Discussion)
class DiscussionAdmin(ImportExportModelAdmin, BaseAdmin):
    """Admin for Discussion model."""

    ordering = ["-created_at"]
    search_fields = ["topic_id"]
    list_display = ["topic_id", "content", "is_available"]
    list_filter = ["is_available", "topic_id"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    resource_class = DiscussionResource
