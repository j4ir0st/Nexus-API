class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Solo agregamos las cabeceras si el usuario está autenticado
        # para no afectar el rendimiento de las páginas públicas.
        if hasattr(request, 'user') and request.user.is_authenticated:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate, private'
        return response
