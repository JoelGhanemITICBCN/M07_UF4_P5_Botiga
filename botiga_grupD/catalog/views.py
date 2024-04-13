from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producte, Cataleg
from .serializers import *

@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    elif request.method == 'POST':
        return Response({"message": "POST request received"})
    elif request.method == 'DELETE':
        return Response({"message": "DELETE request received"})

#Defineix com s-han de mostrar les views de la api a django
@api_view(['GET'])
def mostrar_producte(request, producte_id=None):
    if producte_id:
        try:
            producte = Producte.objects.get(id=producte_id)
            serializer = ProducteSerializer(producte)
            return Response(serializer.data, status=200)
        except Producte.DoesNotExist:
            return Response({'error': 'No s ha trobat el producte que busques'}, status=404)
    else:
        productes = Producte.objects.all()
        serializer = ProducteSerializer(productes, many=True)
        return Response(serializer.data, status=200)
@api_view(['POST'])
#Funcio per afegir productes
def afegir_producte(request, producte_id=None):
        serializer = ProducteSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)

@api_view(['PUT'])
#Funcio per actualitzar productes
def actualitzar_producte(request, producte_id=None):
        producte = Producte.objects.get(id=producte_id)
        serializer = ProducteSerializer(producte, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def eliminar_producte(request, producte_id=None):
    try:
        producte = Producte.objects.get(id=producte_id)
    except Producte.DoesNotExist:
        return Response({'error': 'No s ha trobat el producte que busques'}, status=404)

    # Serializar el producto antes de eliminarlo
    serializer = ProducteSerializer(producte)

    # Eliminar el producto
    producte.delete()

    # Devolver los datos serializados del producto eliminado
    return Response(serializer.data, status=200)
