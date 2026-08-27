from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import *

class SiteRootView(APIView):
    """
    La vista principal del sitio. Muestra los enlaces a las áreas principales: el panel de Administración y la raíz de la API.
    """
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({
            'admin': reverse('admin:index', request=request, format=format),
            'api': reverse('api-root', request=request, format=format),
        })

class APIRootView(APIView):
    """
    La vista raíz de la API. Enumera todas las APIs de las aplicaciones disponibles.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Para que esto funcione, necesitamos nombrar nuestras URLs de la app en el archivo urls.py principal
        return Response({
            'accounts': reverse('accounts:api-root', request=request, format=format),
            'facturacion': reverse('facturacion:api-root', request=request, format=format),
        })
