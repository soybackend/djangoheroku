from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200, blank=True, null=True)    