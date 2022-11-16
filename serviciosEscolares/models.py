from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50,primary_key=True)
    semestre = models.CharField(max_length=50)
    carrera = models.ForeignKey('Carreras', on_delete=models.CASCADE)
    

class Carreras(models.Model):
    claveCarrera = models.CharField(max_length=10,primary_key=True)
    nombreCarrera = models.CharField(max_length=50)
    numeroCreditos = models.IntegerField()
    numeroSemestres = models.IntegerField()
    Coordinador = models.ForeignKey('Docentes', on_delete=models.CASCADE)
    
    
class Docentes(models.Model):
    numeroPersonal = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    #Tipo de docente : Profesor, Jefe de departamento, Coordinador de carrera, etc.
    tipoDocente = models.CharField(max_length=50,choices=[('Profesor','Profesor'),('Jefe de departamento','Jefe de departamento'),('Coordinador de carrera','Coordinador de carrera')])
    correoInstitucional = models.EmailField()

class Tramites(models.Model):
    claveTramite = models.AutoField(primary_key=True)
    nombreTramite = models.CharField(max_length=50)
    descripcionTramite = models.CharField(max_length=50)
    #Tipo de tramite : Inscripcion, reinscripcion, cambio de carrera, etc.
    tipoTramite = models.CharField(max_length=50,choices=[('Inscripcion','Inscripcion'),('Reinscripcion','Reinscripcion'),('Cambio de carrera','Cambio de carrera')])
    #Estado del tramite : En proceso, terminado, cancelado, etc.
    estadoTramite = models.CharField(max_length=50,choices=[('En proceso','En proceso'),('Terminado','Terminado'),('Cancelado','Cancelado')])
    alumno = models.ForeignKey('Alumnos', on_delete=models.CASCADE)
    docente = models.ForeignKey('Docentes', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.CharField(max_length=50)
    departamento = models.ForeignKey('Departamentos', on_delete=models.CASCADE)
    
class Departamentos(models.Model):
    claveDepartamento = models.CharField(max_length=10,primary_key=True)
    nombreDepartamento = models.CharField(max_length=50)
    #Tipo de departamento : Administrativo, academico, etc.
    tipoDepartamento = models.CharField(max_length=50,choices=[('Administrativo','Administrativo'),('Academico','Academico')])
    jefeDepartamento = models.ForeignKey('Docentes', on_delete=models.CASCADE)
    