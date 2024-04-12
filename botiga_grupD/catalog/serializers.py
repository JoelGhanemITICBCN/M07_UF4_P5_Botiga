from django.contrib.auth.models import Group, User
from rest_framework import serializers
from botiga_grupD.catalog.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producte
        fields = ['__all__']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cataleg
        fields = ['__all__']