from django.db import models
from django.contrib.auth.models import User

class Galeria(models.Model):
    nombre = models.CharField(max_length=200)
    equipo = models.IntegerField()
    tags    = models.CharField(max_length=250)
    
    def __str__(self):
        
        return self.nombre

class Foto(models.Model):
    galeria = models.ForeignKey(Galeria)
    nombre = models.FileField(max_length=100, upload_to='galeria')
    
    def __str__(self):
        return self.nombre