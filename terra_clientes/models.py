from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    num_doc = models.IntegerField()
    email = models.EmailField(unique=True)
    telefono = models.IntegerField()
    num_dir = models.IntegerField()
    calle = models.CharField(max_length=50)
    localidad = models.CharField(max_length=100, default= 'Desconocido')
    provincia = models.CharField(max_length=100, default= 'Desconocido')
    pais = models.CharField(max_length=100,default= 'Desconocido' )
    fecha_alta = models.DateTimeField(auto_now_add=True)


