from django.db import models
from django.contrib.auth.models import User

from util_request import request_user


class Colegios(models.Model):
    TIPO_CHOICES = [
        (1, 'Clientes'),
        (2, 'No Clientes')
    ]
    SUB_TIPO_CHOICES = [
        (1, 'Contrato Firmado'),
        (2, 'Versión de Prueba'),
        (3, 'Cuentan con Sistema'),
        (4, 'No Cuentan con Sistema')
    ]
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='user_creation', default=request_user)
    tipo = models.IntegerField(choices=TIPO_CHOICES, null=True, blank=True)
    sub_tipo = models.IntegerField(choices=SUB_TIPO_CHOICES, null=True, blank=True)
    nombre_colegio = models.CharField(max_length=1000, null=True, blank=True)
    provincia = models.CharField(max_length=300, null=True, blank=True)
    direccion = models.CharField(max_length=600, null=True, blank=True)
    referencia = models.CharField(max_length=300, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    nombre_promotor = models.CharField(max_length=500, null=True, blank=True)
    nombre_director = models.CharField(max_length=500, null=True, blank=True)
    nombre_secretaria = models.CharField(max_length=500, null=True, blank=True)
    contacto_extra = models.CharField(max_length=500, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if self.sub_tipo == 1 or self.sub_tipo == 2:
    #         self.tipo = 1
    #     else:
    #         self.tipo = 2
    #     super(Colegios, self).save(*args, **kwargs)

    class Meta:
        managed = True
        ordering = ['id']


class Actividades(models.Model):
    colegio = models.ForeignKey(Colegios, on_delete=models.DO_NOTHING, related_name='actividades_colegio')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    observaciones_visita = models.CharField(max_length=1500, null=True, blank=True)

    class Meta:
        managed = True
        ordering = ['-fecha_creacion']
