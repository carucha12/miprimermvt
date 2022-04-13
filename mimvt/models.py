from django.db import models



class familiares(models.Model):
    nombre=models.CharField('nombre',max_length=20)
    apellido=models.CharField('apellido',max_length=20)
    dni=models.IntegerField('dni')
   
    

class profesiones(models.Model):
    profesion=models.CharField('profesion',max_length=20)
    
