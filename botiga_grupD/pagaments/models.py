from django.db import models

# Create your models here.
#Model d usuari per donar li complexitat a pagaments
class Usuari(models.Model):
    nom = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tarjeta = models.CharField(max_length=255)

# Model del carreto temporal per provar que tot funciona, tots els camps son atrezzo menys el pagat
class FakeCarreto(models.Model):
    producte = models.CharField(max_length=255)
    preu = models.IntegerField()
    quantitat = models.IntegerField()
    usuari = models.ForeignKey(Usuari, on_delete=models.CASCADE)
    pagat = models.BooleanField(default=False)

#Exemples del JSON per fer mes facil la insercio de dades

'''
{
    "Usuari":
    
    {
        "nom": "Nombre del usuario",
        "password": "Contraseña del usuario",
        "tarjeta": "Número de tarjeta del usuario"
    },
    "FakeCarreto": 
    
    {
        "producte": "Nombre del producto",
        "preu": 99,
        "quantitat": 1,
        "usuari": 1,
        "pagat": false
    }
    
    
    {
        "pagat": false
    }
}
'''