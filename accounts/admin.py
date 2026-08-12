from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ExtendedUsers

class ExtendedUsersAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(groups__in=request.user.groups.all())

admin.site.register(ExtendedUsers, ExtendedUsersAdmin)
