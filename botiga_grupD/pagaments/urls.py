from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    # Mostra Tots els FakeCarretons
    path('mostra/', views.mostraCarretoFake, name='mostraCarretoFake'),
    # Paga un FakeCarreto
    path('paga/<int:pk>', views.paga, name='paga'),
    # Get all FakeCarretos
    path('fake_carretos/', views.get_fake_carretos, name='get_fake_carretos'),
    # Create a new FakeCarreto
    path('fake_carretos/create/', views.create_fake_carreto, name='create_fake_carreto'),
    # Get all Usuaris
    path('usuaris/', views.get_usuaris, name='get_usuaris'),
    # Create a new Usuari
    path('usuaris/create/', views.create_usuari, name='create_usuari'),
]