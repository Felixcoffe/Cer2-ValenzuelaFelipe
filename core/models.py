from django.db import models

# Create your models here.

class Residencia(models.Model):
    Num_residencia=models.IntegerField()
    Propietario=models.CharField(max_length=30)
    Estado_viv= (
        ('Ocupado','Ocupado'),
        ('Disponible','Disponible'),
        ('En Mantenimiento','En mantenimiento')
        )
    Estado = models.CharField(max_length=30, choices= Estado_viv)

class Correspondencia(models.Model):
    fecha_llegada= models.DateField()
    Destino= models.IntegerField(null=True)
    Estado_Cor= (
        ('En Consejeria','En Consejeria'),
        ('Entregada','Entregada')
    ) 
    Estado = models.CharField(max_length=30, choices=Estado_Cor)
