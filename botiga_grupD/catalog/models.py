from django.db import models

#Models de producte i cataleg relacionats amb FK per id_producte
class Producte(models.Model):
    nom = models.CharField(max_length=255)
    preu = models.FloatField()
    stock = models.IntegerField()
    descripcio = models.CharField(max_length=255)
    pes = models.FloatField()
    subcategoria = models.CharField(max_length=255)

"""
{
    "nom": "Producto 1",
    "preu": 99.99,
    "stock": 100,
    "descripcio": "Descripción del producto",
    "pes": 1.5,
    "subcategoria": "Subcategoría del producto"
}
"""