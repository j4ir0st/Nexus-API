from django.urls import path, include
from nexus_api.views import SiteRootView, APIRootView
from .admin_site import custom_admin_site
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# URLs de las aplicaciones de la API
api_urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('facturacion/', include(('facturacion.urls', 'facturacion'), namespace='facturacion')),
]

# URLs principales del proyecto
urlpatterns = [
    path('', SiteRootView.as_view(), name='site-root'),
    path('admin/', custom_admin_site.urls),
    path('api/', include(api_urlpatterns)),
    path('api-auth/', include('rest_framework.urls')),
    path('get-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]
