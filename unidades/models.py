from django.db import models

# Create your models here.
class unidades(models.Model):
    nomenclatura = models.CharField(primary_key=True, null=False, max_length=4)
    patente = models.CharField(max_length=8)
    estadoUnidad = models.BooleanField(default=True)
    especialidad = models.CharField(max_length=15)
    comentario = models.TextField()

def getunidad(self):
    unidad = {"nomenclatura" : self.nomenclatura, "patente" : self.patente, 
              "estadoUnidad" : self.estadoUnidad, "especialidad" : self.especialidad,
              "comentario" : self.comentario}
    return unidad

def setNomenclatura(self, nvaNomenclatura):
    self.nomenclatura = nvaNomenclatura

def setPatente(self, nvaPatente):
    self.patente = nvaPatente

def setEstadoUnidad(self, nvoEstado):
    self.estadoUnidad = nvoEstado

def setEspecialidad(self, nvaEspecialidad):
    self.especialidad = nvaEspecialidad

def setComentario(self, nvoComentario):
    self.comentario = nvoComentario