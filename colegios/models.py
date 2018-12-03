from django.db import models
from django.contrib.auth.models import User


# from custom_middleware.current_user import

class Colegios(models.Model):
    SEX_CHOICES = [
        (1, 'Masculino'),
        (2, 'Femenino')
    ]
    TIPO_CHOICES = [
        (1, 'Clientes'),
        (2, 'No Clientes')
    ]
    SEX_CHOICES = [
        (1, 'Masculino'),
        (2, 'Femenino')
    ]
    SEX_CHOICES = [
        (1, 'Masculino'),
        (2, 'Femenino')
    ]
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='user_creation')
    # sexo = models.IntegerField(choices=SEX_CHOICES, null=True, blank=True)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    direccion = models.CharField(max_length=300, null=True, blank=True)
    # -------------------
    direccion = models.CharField(max_length=300, null=True, blank=True)
    referencia = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        managed = True
        ordering = ['id']
