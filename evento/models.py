from django.db import models

# Create your models here.

class Evento(models.Model):
    nombre   = models.CharField(max_length=200)
    fecha    = models.DateField('date published')
    imagen   = models.CharField(max_length=200)
    descripcion = models.TextField()
	usuario  - models.IntegerField()
    
	def __str__(self):
		return self.nombre


class FotoEvento(models.Model):
	foto   = models.ForeignKey(Evento)

	def __str__(self):
		return self.foto

 Evento
 	nombre
	fecha
	imagen
	descripcion
	fotografias_previas fk
	usuario

