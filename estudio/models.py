from django.contrib.auth.models import Group, User #importa los modelos Group y user
from django.db import models #importa los metodos necesarios para trabajar con modellos

class Paciente(models.Model):
    rut = models.CharField(max_length=100, null=True, blank=True, verbose_name='Rut Paciente')
    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre Paciente')
    telefono = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telefono Paciente')
    Sexo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Sexo Paciente')
    correo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Correo Paciente')
    edad = models.CharField(max_length=100, null=True, blank=True, verbose_name='Edad Paciente')
    direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Direccion Paciente')
    estado = models.CharField(max_length=100, null=True, blank=True, default='Activo', verbose_name='Estado')   
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['nombre']   
    def __str__(self):
        return self.nombre
    
class Cita(models.Model):
    fechaAtencion = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Atencion')
    horaInicio = models.DateTimeField(auto_now_add=True,verbose_name='Hora Inicio')
    horaFinal = models.DateTimeField(auto_now_add=True,verbose_name='Hora Final')
    procedimiento = models.CharField(max_length=100, null=True, blank=True, verbose_name='Procedimiento Paciente')
    diagnostico = models.CharField(max_length=100, null=True, blank=True, verbose_name='Diagnostico Paciente')
    extra = models.CharField(max_length=100, null=True, blank=True, verbose_name='Extra Paciente')
    estado = models.CharField(max_length=100, null=True, blank=True, default='Activo', verbose_name='Estado')
    
class Trabajador(models.Model):
    rut = models.CharField(max_length=100, null=True, blank=True, verbose_name='Rut Trabajador')
    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre Trabajador')
    telefono = models.CharField(max_length=100, null=True, blank=True, verbose_name='Telefono Trabajador')
    Sexo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Sexo Trabajador')
    correo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Correo Trabajador')
    edad = models.CharField(max_length=100, null=True, blank=True, verbose_name='Edad Trabajador')
    direccion = models.CharField(max_length=100, null=True, blank=True, verbose_name='Direccion Trabajador')
    estado = models.CharField(max_length=100, null=True, blank=True, default='Activo', verbose_name='Estado')   
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')
    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'
        ordering = ['nombre']   
    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre Cargo')
    estado = models.CharField(max_length=100, null=True, blank=True, default='Activo', verbose_name='Estado')
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargo'
        ordering = ['nombre']   
    def __str__(self):
        return self.nombre