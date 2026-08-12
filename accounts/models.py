from django.contrib.auth.models import AbstractUser
from django.db import models

class ExtendedUsers(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')], null=True, blank=True)
    nro_telefono = models.CharField(max_length=20, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    talla = models.CharField(max_length=3, null=True, blank=True)
    miembro = models.BooleanField(null=True, blank=True)
    estaca = models.CharField(max_length=60, null=True, blank=True)
    barrio = models.CharField(max_length=120, null=True, blank=True)
    grupo_sanguineo = models.CharField(max_length=12, null=True, blank=True)
    enfermedad = models.CharField(max_length=240, null=True, blank=True)
    tratamiento = models.CharField(max_length=240, null=True, blank=True)
    seguro = models.CharField(max_length=60, null=True, blank=True)
    persona_contacto = models.CharField(max_length=120, null=True, blank=True)
    telefono_contacto = models.CharField(max_length=60, null=True, blank=True)
