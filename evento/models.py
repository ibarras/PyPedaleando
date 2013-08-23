from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Evento(models.Model):
    nombre   = models.CharField(max_length=200)
    fecha    = models.DateField('date published')
    imagen   = models.FileField(max_length=200, upload_to = 'eventos')
    descripcion = models.TextField()
    usuario     = models.ForeignKey(User)
    
    def __str__(self):
        return self.nombre

class Foto(models.Model):
    evento = models.ForeignKey(Evento)
    foto = models.FileField(max_length=100, upload_to = 'eventos')
    
    def __str__(self):
        return self.foto