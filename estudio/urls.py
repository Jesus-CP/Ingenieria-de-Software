from django.conf.urls import url #importa la función url
from django.urls import path #importa el metodo path
from estudio import views #importará los métodos que generemos en nuestra app

estudio_urlpatterns = [
    path('main/', views.main, name="main"),
    ]

    