from nexus_api.admin_site import custom_admin_site
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import *


# --- Admin para ExtendedUsers ---
@admin.register(ExtendedUsers, site=custom_admin_site)
class ExtendedUsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')

# --- Admin para LogEntry ---
@admin.register(CustomLogEntry, site=custom_admin_site)
class CustomLogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_repr',
        'action_flag',
    ]
    readonly_fields = [f.name for f in LogEntry._meta.fields] + ['user']
    search_fields = ['user__username', 'object_repr', 'change_message']
    list_filter = ['action_flag', 'content_type']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

