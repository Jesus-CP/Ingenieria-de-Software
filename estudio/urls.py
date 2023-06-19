from django.conf.urls import url #importa la función url
from django.urls import path #importa el metodo path
from estudio import views #importará los métodos que generemos en nuestra app
from core.views import check_profile

estudio_urlpatterns = [
    path('index/', views.index, name="index"),
    path('paciente/', views.paciente, name="paciente"),
    path('odontologo/', views.odontologo, name="odontologo"),
    path('agendarCita/', views.agendarCita, name="agendarCita"),
    path('verCita/', views.verCita, name="verCita"),
    path('crear_odontologo/', views.crear_odontologo, name="crear_odontologo"),
    path('odontologo_save/', views.odontologo_save, name="odontologo_save"),
    path('crear_paciente/', views.crear_paciente, name="crear_paciente"),
    path('paciente_save/', views.paciente_save, name="paciente_save"),
    path('cita_save/',views.cita_save,name="cita_save"),
    path('ver_agenda/<offset>/',views.ver_agenda,name="ver_agenda"),
    path('verCitas/', views.verCita, name="verCita"),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    ]

    