from rest_framework import permissions, viewsets, filters, views
from django.db.models import Value, CharField, IntegerField
from rest_framework.pagination import PageNumberPagination
import django_filters.rest_framework as df
from rest_framework import status
from django.conf import settings
from .serializers import *
from .filters import *
from .models import *

# Create your views here.
class ExtendedUsersViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite obtener los [**Usuarios**][ref3] que tienen acceso a las aplicaciones y a la [**API**][ref].

    [ref]: https://
    """
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.DjangoModelPermissions]
        else:
            permission_classes = [permissions.DjangoModelPermissions]
        return [permission() for permission in permission_classes]
    
    # schema = Users_Schema()
    queryset = ExtendedUsers.objects.all().order_by('-id')
    serializer_class = ExtendedUserSerializer
    filter_backends = [df.DjangoFilterBackend, filters.OrderingFilter]
    permission_classes = get_permissions
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'top'
    pagination_class.max_page_size = 1000
    filterset_class = ExtendedUsersFilter