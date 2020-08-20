
from django.db import models

# Create your models here.
class Libro(models.Model):
    editorial = models.CharField(max_length=20, default="");

class Material(models.Model):
    codigo = models.CharField(max_length=20, default="")
    autor = models.CharField(max_length=20, default="")
    titulo = models.CharField(max_length=20, default="")
    ano = models.IntegerField(null = True)
    status = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.titulo)

class Libro(Material):
    editorial = models.CharField(max_length=20, default="")


class Revista(Material):
    numero = models.IntegerField(null = True)

class Persona(models.Model):
    nombre = models.CharField(max_length=20, default="")
    apellido = models.CharField(max_length=20, default="")
    correo = models.CharField(max_length=20, default="")
    telefono = models.IntegerField(null = True)
    NumLibros = models.IntegerField(null=True)
    adeudo = models.FloatField(null = True)

    def __str__(self):
        return str(self.nombre + " " + self.apellido)

class Alumno(Persona):
    matricula = models.IntegerField(null = True)

class Profesor(Persona):
    numEmpleado = models.IntegerField(null = True)

class Prestamo(models.Model):
    persona = models.ForeignKey( 'Persona', on_delete=models.CASCADE)
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    fechaSalida = models.DateField(auto_now=True)
    fechaRegreso = models.DateField()

    def __str__(self):
        return str(self.persona.nombre + " " + self.material.titulo)