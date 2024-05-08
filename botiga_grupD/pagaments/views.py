from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import FakeCarreto
from .serializers import *
from .serializers import FakeCarretoSerializer

# Create your views here.
#View per modificar el valor de pagat
@api_view(['PUT'])
def paga(request, pk):
    #Cas de que no troba el carreto
    try:
        paga = FakeCarreto.objects.get(id=pk)
    except FakeCarreto.DoesNotExist:
        return Response({'error': 'FakeCarreto not found'}, status=404)

    #Cas en el que troba el carreto 
    serializer = FakeCarretoSerializer(paga, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

#Mostra tots els carretons
@api_view(['GET'])
def mostraCarretons(request, category_id=None):
        mostra = FakeCarreto.objects.all()
        serializer = MostraFakeSerializer(mostra, many=True)
        return Response(serializer.data, status=200)

#Crea un carreto Fake
@api_view(['POST'])
def create_fake_carreto(request):
    serializer = MostraFakeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

#Mostra un usuari
@api_view(['GET'])
def get_usuaris(request):
    usuaris = Usuari.objects.all()
    serializer = UsuariSerializer(usuaris, many=True)
    return Response(serializer.data, status=200)

#Crea un Usuari
@api_view(['POST'])
def create_usuari(request):
    serializer = UsuariSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)