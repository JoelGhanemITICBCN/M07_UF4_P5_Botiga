from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  
from .models import FakeCarreto
from .serializers import *
from .serializers import FakeCarretoSerializer

# Create your views here.
@api_view(['PUT'])
def paga(request, pk):
    try:
        paga = FakeCarreto.objects.get(id=pk)
    except FakeCarreto.DoesNotExist:
        return Response({'error': 'FakeCarreto not found'}, status=404)

    serializer = MostraFakeSerializer(paga, data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def mostraCarretoFake(request, category_id=None):
        mostra = FakeCarreto.objects.all()
        serializer = MostraFakeSerializer(mostra, many=True)
        return Response(serializer.data, status=200)

@api_view(['GET'])
def get_fake_carretos(request):
    fake_carretos = FakeCarreto.objects.all()
    serializer = FakeCarretoSerializer(fake_carretos, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def create_fake_carreto(request):
    serializer = FakeCarretoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_usuaris(request):
    usuaris = Usuari.objects.all()
    serializer = UsuariSerializer(usuaris, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def create_usuari(request):
    serializer = UsuariSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)