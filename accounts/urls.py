from django.urls import path, include
from rest_framework import routers
from . import views

# El router genera automáticamente las URLs para los ViewSets
router = routers.DefaultRouter()
router.register(r'users', views.ExtendedUsersViewSet, basename='extendedusers')

# Las URLs de la API para la app de accounts
urlpatterns = [
    # La raíz de la API de esta app, muestra los enlaces a los endpoints de abajo
    path('', views.AccountsAPIRootView.as_view(), name='api-root'),
    # Incluye las URLs generadas por el router
    path('', include(router.urls)),
]
