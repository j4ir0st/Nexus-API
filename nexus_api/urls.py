from django.contrib import admin
from django.urls import path, include
from nexus_api.views import APIRootView

urlpatterns = [
    path('', APIRootView.as_view()),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
