from django.db import models

#Models de producte i cataleg relacionats amb FK per id_producte
class Producte(models.Model):
    nom = models.CharField(max_length=255)
    preu = models.FloatField()
    stock = models.IntegerField()
    descripcio = models.CharField(max_length=255)
    pes = models.FloatField()
    subcategoria = models.CharField(max_length=255)

class Cataleg(models.Model):
    id_producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)

class Targeta(models.Model):
    num_targeta = models.CharField(max_length=255)
    caducitat = models.DateField()
    codi_seguretat = models.IntegerField()

class Usuari(models.Model):
   nom = models.CharField(max_length=255)
   cognom = models.CharField(max_length=255)
   validat = models.BooleanField()
   id_targeta = models.ForeignKey(Targeta, on_delete=models.CASCADE)
   passwd = models.CharField(max_length=255)