from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sexo(models.Model):
    sexo = models.CharField(max_length=20)

    def __str__(self):
        return self.sexo

class Estado(models.Model):
    nombre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Medico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.first_name

class Enfermero(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
    

class Paciente(models.Model):
    img = models.ImageField(upload_to='pacientes', null=True, blank=True)
    ci=models.CharField(max_length=11)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    direccion = models.CharField(max_length=300)
    municipio = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    cod_postal = models.CharField(max_length=20)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=100)
    correo = models.EmailField(null=True, blank=True)
    edad = models.IntegerField()
    telf_movil = models.CharField(max_length=8)
    telf_fijo = models.CharField(max_length=8)
    observaciones = models.TextField()

    def __str__(self):
        return self.nombre+' '+self.apellidos

class Historia_clinica(models.Model):
    numero = models.IntegerField()
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)
    
    
