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
@api_view(['POST'])
#Funcio per afegir productes
def afegir_producte(request, producte_id=None):
    if request.method == 'POST':
        serializer = ProducteSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)