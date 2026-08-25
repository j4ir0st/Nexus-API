from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # 1. Definimos la estructura de datos base para las secciones
        secciones_config = {
            'Autorizacion_Admin': {'name': 'Autorización', 'models': [], 'match': ['ExtendedUsers', 'Group', 'EU_Oficina', 'EU_Area', 'EU_Puestos', 'TokenProxy', 'Token']},
            'Facturacion_Admin': {'name': 'Facturación', 'models': [ 'Fact_Detalle', 'Facturas', 'Fact_UpdateAudit']},
            # 'Guias_Admin': {'name': 'Guías de Remisión', 'models': ['GR_Descripcion', 'GuiasRemision', 'GR_Regularizacion','GR_UpdateAudit', 'GD_Descripcion', 'Guia_Digemid']},
            # 'HojaPicking_Admin': {'name': 'Hoja Picking', 'models': ['HojaPicking', 'HP_UpdateAudit', 'HP_ListaBlanca', 'HP_ScanProductos']},
            # 'Licitaciones_Admin': {'name': 'Licitaciones', 'models': ['Lic_TipoProceso', 'Lic_Entidad', 'Lic_Estado', 'Lic_Productos', 'Licitaciones', 'Lic_UpdateAudit']},
            # 'RotuladoBultos_Admin': {'name': 'Rotulado Bultos', 'models': ['RB_Consignatario', 'RB_DestinoCatalogo', 'RB_DestinosEtiqueta', 'RB_GuiasRemision', 'RB_Representante', 'RotuladoBultos', 'RB_UpdateAudit']},
            # 'StockAprobados_Admin': {'name': 'Stock Aprobados', 'models': ['SA_Familia', 'SA_Categoria', 'SA_TipoCategoria', 'StockAprobado', 'Stock_ERP']},
            # 'StockInventario_Admin': {'name': 'Stock Inventario', 'models': ['SI_Empresa', 'SI_Linea', 'SI_Grupo', 'SI_Familia', 'SI_Proveedor', 'SI_Producto', 'SI_Deposito', 'SI_Sector', 'SI_TipoAlmacen', 'SI_Transito', 'SI_Kits', 'SI_Descripcion', 'StockInventario', 'SI_UpdateAudit']},
            # 'Vacaciones_Admin': {'name': 'Vacaciones', 'models': ['SolicitudVacaciones']},
            # 'CajaChica_Admin': {'name': 'Caja Chica', 'models': ['Requerimiento_CajaChica', 'RC_Detalle', 'RC_Entidades', 'RC_TipoGasto', 'RC_SubGasto', 'RC_Provincia']},
            # 'Otros_Admin': {'name': 'Otros', 'models': ['USR_IDPAPP', 'PA_Pedidos', 'Feedback', 'QR_Productos', 'QR_Update_Audit']}
        }

        # Diccionario intermedio para agrupar solo los modelos a los que el usuario TIENE acceso
        secciones_con_permiso = {label: [] for label in secciones_config.keys()}

        # 2. Mapeamos los modelos permitidos por Django a sus respectivas secciones
        for app in app_list:
            for model in app['models']:
                nombre_modelo = model['object_name']
                
                # Buscamos a qué sección pertenece el modelo
                for app_label, config in secciones_config.items():
                    # Para 'Autorizacion_Admin' usamos su lista 'match', para los demás su lista 'models'
                    lista_modelos = config['match'] if 'match' in config else config['models']
                    
                    if nombre_modelo in lista_modelos:
                        secciones_con_permiso[app_label].append(model)
                        break  # Pasamos al siguiente modelo una vez ubicado

        # 3. Construimos la lista final EXCLUYENDO las secciones que se quedaron vacías
        app_list_personalizada = []
        es_superusuario = request.user.is_superuser
        
        for app_label, config in secciones_config.items():
            modelos_usuario = secciones_con_permiso[app_label]
            
            # FILTRO CRÍTICO: Si el usuario no tiene acceso a ningún modelo de esta sección, no se agrega
            if modelos_usuario or es_superusuario: 
                app_list_personalizada.append({
                    'name': config['name'],
                    'app_label': app_label,
                    'models': modelos_usuario,
                })

        return app_list_personalizada

custom_admin_site = CustomAdminSite(name='my_custom_admin')