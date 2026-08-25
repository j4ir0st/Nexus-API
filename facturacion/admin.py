from django.contrib import admin
from .models import Fact_Empresa, Facturas, Fact_Detalle, Fact_UpdateAudit
from nexus_api.admin_site import custom_admin_site


@admin.register(Fact_Empresa, site=custom_admin_site)
class Fact_EmpresaAdmin(admin.ModelAdmin):
    list_display = ('empresa',)
    search_fields = ('empresa',)

@admin.register(Facturas, site=custom_admin_site)
class FacturasAdmin(admin.ModelAdmin):
    list_display = ('nro_fact', 'nombre_cliente', 'fecha_emision', 'monto', 'estado', 'empr_id')
    search_fields = ('nro_fact', 'nombre_cliente', 'comprobante')
    list_filter = ('estado', 'cancelado', 'empr_id')
    date_hierarchy = 'fecha_emision'

@admin.register(Fact_Detalle, site=custom_admin_site)
class Fact_DetalleAdmin(admin.ModelAdmin):
    list_display = ('comprobante', 'prod', 'cantidad', 'precio_unit', 'precio_soles')
    search_fields = ('comprobante', 'prod')

@admin.register(Fact_UpdateAudit, site=custom_admin_site)
class Fact_UpdateAuditAdmin(admin.ModelAdmin):
    list_display = ('nro_fact', 'usuario', 'fecha_hora')
    search_fields = ('nro_fact', 'usuario')
    readonly_fields = [f.name for f in Fact_UpdateAudit._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

