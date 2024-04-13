from rest_framework import serializers
from .models import *

class ProducteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producte
        fields = ['__all__']


class CatalegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cataleg
        fields = ['__all__']