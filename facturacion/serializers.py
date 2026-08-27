from rest_framework import serializers
from .models import Fact_Empresa, Facturas, Fact_Detalle, Fact_UpdateAudit

class FactEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact_Empresa
        fields = '__all__'

class FactDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact_Detalle
        fields = '__all__'

class FacturasSerializer(serializers.ModelSerializer):
    # Hacemos que los detalles sean de solo lectura en la vista de lista,
    # pero podemos anidarlos para verlos.
    fd = FactDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Facturas
        fields = '__all__'

class FactUpdateAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact_UpdateAudit
        fields = '__all__'
