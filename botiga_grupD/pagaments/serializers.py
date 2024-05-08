from rest_framework import serializers  
from .models import * 
class FakeCarretoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeCarreto
        fields = ('pagat',)

class MostraFakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeCarreto
        fields = '__all__'
class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = '__all__'