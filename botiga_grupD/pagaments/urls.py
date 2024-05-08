from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    # Mostra Tots els FakeCarretons
    path('mostra/', views.mostraCarretons, name='mostraCarretons'),
    # Paga un FakeCarreto
    path('paga/<int:pk>', views.paga, name='paga'),
    # Crea un FakeCarreto
    path('creaCarreto/', views.create_fake_carreto, name='create_fake_carreto'),
    # Mostra tots els Usuaris
    path('usuaris/', views.get_usuaris, name='get_usuaris'),
    # Crea un nou Usuari
    path('creaUsuaris/', views.create_usuari, name='create_usuari'),
]