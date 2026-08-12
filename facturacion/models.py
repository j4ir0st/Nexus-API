from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import timedelta
from django.db import models


class Fact_Empresa(models.Model):
    empresa = models.CharField(db_column='EMPRESA', max_length=50, blank=True, null=True, help_text='Nombre de la Empresa Asociada.')

    def __str__(self):
        return self.empresa
   
    class Meta:
        managed = True
        db_table = 'FACT_EMPRESA'
        verbose_name = 'Fact Empresa'
        verbose_name_plural = 'Fact Empresas'

class Facturas(models.Model):
    nro_fact = models.CharField(db_column='NUMERO_FACTURA', max_length=20, blank=True, null=True, help_text="Nro de documento de la Boleta o Factura.")
    cod_form = models.CharField(db_column='CODIGO_FORMULARIO', max_length=6, blank=True, null=True, help_text="Código del Formulario de la Boleta o Factura.")
    nro_form = models.IntegerField(db_column='NUMERO_FORMULARIO', blank=True, null=True, help_text="Número del Formulario de la Boleta o Factura.")
    comprobante = models.CharField(db_column='COMPROBANTE', max_length=20, blank=True, null=True, help_text="Número de Comprobante de la Boleta o Factura.")
    fecha_emision = models.DateTimeField(db_column='FECHA_EMISION', blank=True, null=True, help_text="Fecha y Hora en que se generó la Boleta o Factura.")
    monto = models.DecimalField(db_column='MONTO', max_digits=18, decimal_places=2, blank=True, null=True, help_text='Monto Total de la Boleta o Factura.')
    moneda = models.CharField(db_column='MONEDA', max_length=60, blank=True, null=True, help_text='Moneda del Monto Total de la Boleta o Factura.')
    nombre_cliente = models.CharField(db_column='NOMBRE_CLIENTE', max_length=150, blank=True, null=True, help_text='Nombre del cliente.')
    cond_pago = models.CharField(db_column='CONDICION_PAGO', max_length=60, blank=True, null=True, help_text='Condición de Pago.')
    vendedor = models.CharField(db_column='VENDEDOR', max_length=60, blank=True, null=True, help_text='Nombre del Vendedor.')
    cancelado = models.CharField(db_column='CANCELADO', max_length=1, blank=True, null=True, help_text='Estado de cancelación de la Boleta o Factura. S=Cancelado - N=Falta Cancelar')
    estado = models.CharField(db_column='ESTADO', max_length=3, blank=True, null=True, help_text='Estado de la Boleta o Factura. ACT=Activo - ANU=Anulado')
    cobrado = models.DecimalField(db_column='COBRADO', max_digits=18, decimal_places=2, blank=True, null=True, help_text='Monto Cobrado de la Boleta o Factura.')
    saldo = models.DecimalField(db_column='SALDO', max_digits=18, decimal_places=2, blank=True, null=True, help_text='Monto que falta cobrar de la Boleta o Factura.')
    nc_canje_fact = models.CharField(db_column='NC_CANJE_FACTURA', max_length=120, blank=True, null=True, help_text='Factura que tiene Nota de Crédito de Canje.')
    nc_fact_canje = models.CharField(db_column='NC_FACTURA_CANJE', max_length=20, blank=True, null=True, help_text='Nota de Crédito de Canje.')
    nc_anulacion = models.CharField(db_column='NC_ANULACION', max_length=35, blank=True, null=True, help_text='Nota de Crédito de Anulación de Factura.')
    titulo_grat = models.CharField(db_column='TITULO_GRATUITO', max_length=1, blank=True, null=True, help_text='Título gratuito.')
    empr_id = models.ForeignKey(Fact_Empresa, db_column='EMPRESA_ID', on_delete=models.DO_NOTHING, blank=True, null=True, help_text='Número de ID de la empresa asociada responsable de la Boleta o Factura.')
    dir_entr = models.CharField(db_column='DIRECCION_ENTREGA', max_length=255, blank=True, null=True, help_text='Dirección de Entrega de la Boleta o Factura.')
    dir_fact = models.CharField(db_column='DIRECCION_FACTURACION', max_length=60, blank=True, null=True, help_text='Dirección de Facturación.')
    id_app = models.IntegerField(db_column='ID_APP', blank=True, null=True, help_text='ID del Formulario de Solicitud de Pedidos relacionada a la Boleta o Factura.')
    oc_cliente = models.CharField(db_column='OC_CLIENTE', max_length=20, blank=True, null=True, help_text='Nro de Orden de Compra de la Boleta o Factura.')
    tipo_cliente = models.CharField(db_column='TIPO_CLIENTE', max_length=60, blank=True, null=True, help_text="Tipo de Cliente. PÚBLICO o PRIVADO")
    tipo_venta = models.CharField(db_column='TIPO_VENTA', max_length=6, blank=True, null=True, help_text="Tipo de Venta. Permite excluir CANJES")
    usuario_registro = models.CharField(db_column='USUARIO_REGISTRO', max_length=15, blank=True, null=True, help_text="Usuario que generó la Boleta o Factura.")
    zona = models.CharField(db_column='ZONA', max_length=60, blank=True, null=True, help_text="Nombre de la Zona de Entrega.")
    afecto_detr = models.CharField(db_column='AFECTO_DETRACCION', max_length=1, blank=True, null=True, help_text="Verifica si Corresponde Detracción. S=Sí - N=No")
    afecto_ret = models.CharField(db_column='AFECTO_RETENCION', max_length=1, blank=True, null=True, help_text="verifica si Corresponde Retención. S=Sí - N=No")
    monto_soles = models.DecimalField(db_column='MONTO_SOLES', max_digits=18, decimal_places=2, blank=True, null=True, help_text="Monto Total en Soles de la Boleta o Factura.")
    usuario = models.CharField(db_column='USUARIO', max_length=120, blank=True, null=True, help_text="Usuario que modificó la Boleta o Factura.")

    def __str__(self):
        return f"{self.nro_fact} - {self.empr_id}"
    
    class Meta:
        managed = True
        db_table = 'FACT_DETALLE'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

class Fact_Detalle(models.Model):
    comprobante = models.CharField(db_column='COMPROBANTE', max_length=20, blank=True, null=True, help_text="Número de Comprobante de la Boleta o Factura.")
    nro_item = models.IntegerField(db_column='NUMERO_ITEM', blank=True, null=True, help_text='Nro de Item del Producto de la Boleta o Factura.')
    tipo_producto = models.CharField(db_column='TIPO_PRODUCTO', max_length=6, blank=True, null=True, help_text='Tipo de Producto.')
    prod = models.CharField(db_column='PRODUCTO', max_length=30, blank=True, null=True, db_index=True, help_text='Nro de Serie del Producto.')
    cantidad = models.DecimalField(db_column='CANTIDAD', max_digits=18, decimal_places=2, blank=True, null=True, help_text='Cantidad de Productos por Lote.')
    precio_unit = models.DecimalField(db_column='PRECIO_UNITARIO', max_digits=18, decimal_places=2, blank=True, null=True, help_text='Precio unitario en Soles del Producto de la Boleta o Factura.')
    precio_soles = models.DecimalField(db_column='PRECIO_SOLES', max_digits=18, decimal_places=2, blank=True, null=True, help_text="Precio Total en Soles del Producto de la Boleta o Factura. CANTIDAD x PRECIO_UNITARIO")
    fact_id = models.ForeignKey(Facturas, on_delete=models.CASCADE, db_column='FACT_ID', related_name='fd', blank=True, null=True, db_index=True, help_text='ID único de la Boleta o Factura.')
    comision_pagada = models.BooleanField(db_column='COMISION_PAGADA', default=False, blank=True, null=True, help_text='Indica si la Comsión de este producto fue pagada al respectivo representante.')
    comision_pagada_sup = models.BooleanField(db_column='COMISION_PAGADA_SUPERVISOR', default=False, blank=True, null=True, help_text='Indica si la Comsión de este producto fue pagada al respectivo Supervisor.')
    usuario = models.CharField(db_column='USUARIO', max_length=120, blank=True, null=True, help_text="Usuario que modificó los items de la Boleta o Factura.")

    def __str__(self):
        return f"{self.comprobante}"
    
    class Meta:
        managed = True
        db_table = 'FACTURAS'
        verbose_name = 'Factura Detalle'
        verbose_name_plural = 'Facturas Detalle'

class Fact_UpdateAudit(models.Model):
    id_fact = models.IntegerField(db_column='ID_FACT', blank=True, null=False, help_text='ID único de la Boleta o Factura.')
    nro_fact = models.CharField(db_column='NUMERO_FACTURA', max_length=20, blank=True, null=True, help_text="Nro de documento de la Boleta o Factura.")
    empr_id = models.ForeignKey(Fact_Empresa, db_column='EMPRESA_ID', related_name='empr_audit',on_delete=models.DO_NOTHING, blank=True, null=True, help_text='Número de ID de la empresa asociada responsable de la Boleta o Factura.')
    estado_old = models.TextField(db_column='ESTADO_OLD', blank=True, null=True, help_text='Estado del registro antes de hacer las modificaciones.')
    estado_new = models.TextField(db_column='ESTADO_NEW', blank=True, null=True, help_text='Estado del registro después de hacer las modificaciones.')
    fecha_hora = models.DateTimeField(db_column='FECHA_HORA', blank=True, null=True, help_text='Fecha y Hora en la que el usuario que realizo modificaciones en el registro.')
    usuario = models.CharField(db_column='USUARIO', max_length=60, blank=True, null=True, help_text='Nombre del usuario que realizo modificaciones en el registro.')

    def __str__(self):
        return f"{self.nro_fact} - {self.empr_id}"
    
    class Meta:
        managed = True
        db_table = 'FACT_UPDATE_AUDIT'
        verbose_name = 'Fact Audit'
        verbose_name_plural = 'Fact Audits'