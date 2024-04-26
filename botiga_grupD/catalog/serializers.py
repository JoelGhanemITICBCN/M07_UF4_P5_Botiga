from rest_framework import serializers
from .models import *

#Defineix que es mostra a les trucades de la api
class ProducteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = '__all__'

