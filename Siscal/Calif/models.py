from django.db import models

# Create your models here.

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=30, blank=False, null=True)
    Apellido = models.CharField(max_length=50, blank=False, null=True)
    Cedula = models.CharField(primary_key=True, unique=True, max_length=10,blank=False)
    Fecha_de_Nacimiento = models.DateField()
    Correo = models.EmailField(unique=True, blank=False)
    Celular = models.CharField(max_length=10, null=True)

    def __str__(self):
       return self.Cedula

class Docente(models.Model):
    Nombre = models.CharField(max_length=30, blank=False, null=True)
    Apellido = models.CharField(max_length=50, blank=False, null=True)
    Cedula = models.CharField(primary_key=True, unique=True, max_length=10,blank=False)
    Correo = models.EmailField(unique=True, blank=False)
    Celular = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.Nombre
    
class Materia(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    Nombre = models.CharField(max_length=30, blank=False, null=True)
    Cedula = models.ForeignKey(Docente, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Nombre
    
class Nota(models.Model):
    id = models.AutoField(primary_key=True)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.RESTRICT)
    Materia = models.ForeignKey(Materia, on_delete=models.RESTRICT)
    Calificacion = models.FloatField()
    
    def __Float__  (self):
        return self.id