from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    # Mostra Tots els FakeCarretons
    path('mostra/', views.mostraCarretoFake, name='mostraCarretoFake'),
    # Paga un FakeCarreto
    path('paga/<int:pk>', views.paga, name='paga'),
    # Mostra tots els FakeCarretos
    path('fake_carretos/', views.get_fake_carretos, name='get_fake_carretos'),
    # Crea un FakeCarreto
    path('fake_carretos/create/', views.create_fake_carreto, name='create_fake_carreto'),
    # Mostra tots els Usuaris
    path('usuaris/', views.get_usuaris, name='get_usuaris'),
    # Crea un nou Usuari
    path('usuaris/create/', views.create_usuari, name='create_usuari'),
]