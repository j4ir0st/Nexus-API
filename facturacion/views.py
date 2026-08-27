from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .serializers import *
from .models import *



class FacturacionAPIRootView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response({
            'empresas': reverse('facturacion:fact_empresa-list', request=request, format=format),
            'facturas': reverse('facturacion:facturas-list', request=request, format=format),
            'detalles': reverse('facturacion:fact_detalle-list', request=request, format=format),
            'auditoria': reverse('facturacion:fact_updateaudit-list', request=request, format=format),
        })


class FactEmpresaViewSet(viewsets.ModelViewSet):
    queryset = Fact_Empresa.objects.all()
    serializer_class = FactEmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]


class FacturasViewSet(viewsets.ModelViewSet):
    queryset = Facturas.objects.all()
    serializer_class = FacturasSerializer
    permission_classes = [permissions.IsAuthenticated]


class FactDetalleViewSet(viewsets.ModelViewSet):
    queryset = Fact_Detalle.objects.all()
    serializer_class = FactDetalleSerializer
    permission_classes = [permissions.IsAuthenticated]


class FactUpdateAuditViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fact_UpdateAudit.objects.all()
    serializer_class = FactUpdateAuditSerializer
    permission_classes = [permissions.IsAuthenticated]
