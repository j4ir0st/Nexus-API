from rest_framework_simplejwt import serializers as jwt_serializers
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import *


class ExtendedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtendedUsers
        fields = [
            'url', 'username', 'email', 'first_name', 'last_name',
            'is_active', 'date_joined', 'is_staff',
            'avatar', 'nickname', 'fecha_nacimiento', 'sexo',
            'nro_telefono', 'edad', 'talla', 'miembro', 'estaca',
            'barrio', 'grupo_sanguineo', 'enfermedad', 'tratamiento',
            'seguro', 'persona_contacto', 'telefono_contacto'
        ]
