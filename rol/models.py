from django.db import models
from empleado.models import Empleado

# Create your models here.

class Rol(models.Model): 
    id_empleado= models.ForeignKey(Empleado, on_delete=models.CASCADE) 
    aniomes = models.DateField()#202501 
    sueldo = models.DecimalField(max_digits=10, decimal_places=2) 
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2) 
    bono = models.DecimalField(max_digits=10, decimal_places=2) 
    iess = models.DecimalField(max_digits=10, decimal_places=2) 
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2) 
    tot_des = models.DecimalField(max_digits=10, decimal_places=2) 
    neto = models.DecimalField(max_digits=10, decimal_places=2)