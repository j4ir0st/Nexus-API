from ServidorCaminitos.models import ExtendedUsers
from django.contrib.admin.models import LogEntry
from .admin_site import custom_admin_site
from django.contrib import admin
from django.db import models


class CustomLogEntry(LogEntry):
    class Meta:
        proxy = True

    user = models.ForeignKey(
        ExtendedUsers,
        on_delete=models.CASCADE,
        db_constraint=True,
    )


# Reemplazar el modelo original en el admin
admin.site.unregister(LogEntry)

@admin.register(CustomLogEntry, site=custom_admin_site)
class CustomLogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_repr']
    readonly_fields = ['action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message']