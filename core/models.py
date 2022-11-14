from django.db import models

# Create your models here.

class Residencia(models.Model):
    Num_residencia=models.IntegerField()
    Propietario=models.CharField(max_length=30, default="Hoteleria")
    Estado_viv= (
        ('Ocupado','Ocupado'),
        ('Disponible','Disponible'),
        ('En Mantenimiento','En mantenimiento')
        )
    Estado = models.CharField(max_length=30, choices=Estado_viv)
    def __str__(self):
        return 'vivienda %s Estado: %s' % (self.Num_residencia, self.Estado)
    

class Correspondencia(models.Model):
    fecha_llegada= models.DateField()
    nombre= models.CharField(max_length=30, null=True)
    Destino= models.IntegerField(null=True)
    Estado_Cor= (
        ('En Consejeria','En Consejeria'),
        ('Entregada','Entregada')
    ) 
    Estado = models.CharField(max_length=30, choices=Estado_Cor)
    fecha_entregado= models.DateField(null=True, blank=True)
    def __str__(self):
        return '%s %s %s' % (self.nombre, self.Destino, self.Estado)
    
