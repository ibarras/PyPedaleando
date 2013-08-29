from django.db import models
    
class Estado(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    estado = models.ForeignKey(Estado)
    
    def __str__(self):
        return self.nombre
    
class GrupoCiclista(models.Model):    
    nombre  = models.CharField(max_length=200)
    correo  = models.CharField(max_length=200)
    dias    = models.CharField(max_length=200)
    horario = models.TimeField()
    avatar  = models.ImageField(max_length=200, upload_to = 'directorio')
    perfil  = models.ImageField(max_length=200, upload_to = 'directorio')
    texto   = models.TextField()
    
    def __str__(self):
        return self.nombre