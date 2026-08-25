from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({
            'admin': request.build_absolute_uri(reverse('admin:index')),
            'api': request.build_absolute_uri('/accounts'),
        })
