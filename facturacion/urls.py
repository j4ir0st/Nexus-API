from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# El router genera automáticamente las URLs para los ViewSets
router = DefaultRouter()
router.register(r'empresas', views.FactEmpresaViewSet, basename='fact_empresa')
router.register(r'facturas', views.FacturasViewSet, basename='facturas')
router.register(r'detalles', views.FactDetalleViewSet, basename='fact_detalle')
router.register(r'auditoria', views.FactUpdateAuditViewSet, basename='fact_updateaudit')

# Las URLs de la API para la app de facturación
urlpatterns = [
    # La raíz de la API de esta app, muestra los enlaces a los endpoints de abajo
    path('', views.FacturacionAPIRootView.as_view(), name='api-root'),
    # Incluye las URLs generadas por el router
    path('', include(router.urls)),
]
