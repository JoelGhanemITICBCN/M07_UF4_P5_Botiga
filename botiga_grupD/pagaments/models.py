from django.db import models

# Create your models here.
class Usuari(models.Model):
    nom = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tarjeta = models.CharField(max_length=255)

class FakeCarreto(models.Model):
    producte = models.CharField(max_length=255)
    preu = models.IntegerField()
    quantitat = models.IntegerField()
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    pagat = models.BooleanField(default=False)
'''
{
    "Usuari": {
        "nom": "Nombre del usuario",
        "password": "Contraseña del usuario",
        "tarjeta": "Número de tarjeta del usuario"
    },
    "FakeCarreto": {
        "producte": "Nombre del producto",
        "preu": 99,
        "quantitat": 1,
        "usuari": 1,
        "pagat": false
    }
}
'''