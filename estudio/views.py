from django.shortcuts import render
import calendar
import json
import random
from turtle import home
import pandas as pd
from datetime import datetime,timedelta
import locale

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


from django.shortcuts import render
from datetime import datetime, timedelta



from registration.models import Profile
def ver_agenda(request, offset=0):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    fecha_actual = datetime.now().date()
    offset = int(offset)
    inicio_semana = fecha_actual - timedelta(days=fecha_actual.weekday())
    inicio_semana += timedelta(weeks=offset)
    fin_semana = inicio_semana + timedelta(days=6)
    eventos_semana = Cita.objects.filter(fechaAtencion__range=[inicio_semana, fin_semana]).order_by('horaInicio')
    fecha_actual = inicio_semana
    date_range = []
    while fecha_actual <= fin_semana:
        date_range.append(fecha_actual)
        fecha_actual += timedelta(days=1)

    nombres_dias = [
    'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'
    ]
    resultados = [(nombres_dias[fecha.weekday()]+" "+str(fecha.day)) for fecha in date_range]
    print(date_range)

    horarios = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00']

    context = {
        'resultados': resultados,
        'profiles':profiles,
        'eventos_semana': eventos_semana,
        'date_range': date_range,
        'horarios': horarios,
        'inicio_semana': inicio_semana,
        'fin_semana': fin_semana,
        'offset': offset
    }
    
    template_name = 'estudio/ver_agenda.html'
    return render(request,template_name,context)

def index(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/index.html'
    return render(request,template_name,{'profiles':profiles})

def paciente(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/paciente.html'
    return render(request,template_name,{'profiles':profiles})

def odontologo(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/odontologo.html'
    return render(request,template_name,{'profiles':profiles})

def agendarCita(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/agendarCita.html'
    return render(request,template_name,{'profiles':profiles})

def verCita(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1 and profiles.group_id != 2:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'estudio/verCita.html'
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
        return redirect('index')
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
        return redirect('paciente')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')
    


@login_required
def cita_save(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una área para la que no tienes permisos')
        return redirect('check_group_main')

    if request.method == 'POST':
        ODONTOLOGO_DEFAULT = Trabajador.objects.get(id=1)
        PACIENTE_DEFAULT = Paciente.objects.get(id=1)
        fechaAtencion = request.POST.get('fechaAtencion')
        horaInicio = request.POST.get('horaInicio')
        print(fechaAtencion)
        print(horaInicio)

        if  not fechaAtencion or not horaInicio:
            messages.add_message(request, messages.INFO, 'Debes ingresar una hora y fecha para guardar')
            return redirect('agendarCita')


        horaInicio = datetime.strptime(horaInicio, '%H:%M').time()
 
        cita = Cita(
            paciente=PACIENTE_DEFAULT,
            trabajador=ODONTOLOGO_DEFAULT,
            fechaAtencion=fechaAtencion,
            horaInicio=horaInicio,

        )
        cita.save()
        messages.add_message(request, messages.INFO, 'Cita ingresada con éxito')
        return redirect('agendarCita')

    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')