from django.db import models

# Create your models here.
class Usuari(models.Model):
    nom = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tarjeta = models.CharField(max_length=255)