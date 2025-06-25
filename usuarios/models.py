from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Materia(models.Model):
    nombre = models.CharField(max_length=100)  # texto
    cuatrimestre = models.IntegerField()       # número
    fecha_creacion = models.DateField(default=date.today)  # fecha (opcional)

    def __str__(self):
        return self.nombre


class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"

class Archivo(models.Model):
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')
    nombre_original = models.CharField(max_length=255)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_original