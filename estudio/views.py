from django.shortcuts import render
import calendar
import json
import random
from turtle import home
import pandas as pd
from datetime import datetime, time, timedelta


from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, GroupManager, User # Administración de usuarios
from django.utils import timezone
from pytz import timezone as pytz_timezone
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Avg, Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from estudio.models import Paciente, Trabajador,Cita
# Create your views here.

from registration.models import Profile

def main(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/main.html'
    return render(request,template_name,{'profiles':profiles})

@login_required
def crear_odontologo(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/crear_odontologo.html'
    return render(request,template_name,{'profiles':profiles})
@login_required
def odontologo_save(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            messages.add_message(request, messages.INFO, 'Debes ingresar toda la información')
            return redirect('crear_odontologo')
        
        odontologo_save = Trabajador (
            nombre = name,
            state = "O",
            )
        odontologo_save.save()

        messages.add_message(request, messages.INFO, 'Odontologo ingresado con éxito')
        return redirect('main')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')
    
@login_required
def crear_paciente(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/crear_paciente.html'
    return render(request,template_name,{'profiles':profiles})

@login_required
def paciente_save(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        name = request.POST.get('name')

        if not name:
            messages.add_message(request, messages.INFO, 'Debes ingresar toda la información')
            return redirect('crear_paciente')
        
        paciente_save = Paciente (
            nombre = name,
            )
        paciente_save.save()

        messages.add_message(request, messages.INFO, 'Paciente ingresado con éxito')
        return redirect('main')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')
    
@login_required
def crear_cita(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    
    paciente = Paciente.objects.all()
    odontologo = Trabajador.objects.filter(state="O")
    template_name = 'estudio/crear_cita.html'
    context = {
        'odontologo': odontologo,
        'paciente': paciente,
        'profile': profile,
    }
    return render(request, template_name, context)

@login_required
def cita_save(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        trabajador_id = request.POST.get('odontologo')
       #fechaAtencion = request.POST.get('fechaAtencion')
        #horaInicio = request.POST.get('horaInicio')


        if not paciente_id or not trabajador_id: #or not fechaAtencion or not horaInicio:
            messages.add_message(request, messages.INFO, 'Debes ingresar toda la información y seleccionar una categoría')
            return redirect('crear_cita')
        
        paciente = Paciente.objects.get(id=paciente_id)
        trabajador =Trabajador.objects.get(id=trabajador_id)
        cita = Cita(paciente=paciente, trabajador=trabajador)#, fechaAtencion=fechaAtencion, horaInicio=horaInicio)
        cita.save()
        messages.add_message(request, messages.INFO, 'Cita ingresada con éxito')
        return redirect('main')
    
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')