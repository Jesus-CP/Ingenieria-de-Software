from django.conf.urls import url #importa la función url
from django.urls import path #importa el metodo path
from estudio import views #importará los métodos que generemos en nuestra app
from core.views import check_profile

estudio_urlpatterns = [
    path('index/', views.index, name="index"),
    path('paciente/', views.paciente, name="paciente"),
    path('odontologo/', views.odontologo, name="odontologo"),
    path('agendarCita/', views.agendarCita, name="agendarCita"),
    path('cita_save/',views.cita_save,name="cita_save"),
    path('ver_agenda/<offset>/',views.ver_agenda,name="ver_agenda"),
    path('verCitas/', views.verCita, name="verCita"),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('estudio/paciente_ver/<str:paciente_rut>/', views.paciente_ver, name='paciente_ver'),
    path('cancelar_cita/<cita_id>/', views.cancelar_cita, name='cancelar_cita'),

    ]

    