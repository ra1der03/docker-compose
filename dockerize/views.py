from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Animal
from .serializers import AnimalSerializer


@api_view(['GET'])
def getAnimals(request):
    animals = Animal.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAnimal(request, pk):
    animal = Animal.objects.get(id=pk)
    serializer = AnimalSerializer(animal, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addAnimal(request):
    serializer = AnimalSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateAnimal(request, pk):
    animal = Animal.objects.get(id=pk)
    serializer = AnimalSerializer(instance=animal, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteAnimal(request, pk):
    animal = Animal.objects.get(id=pk)
    animal.delete()
    return Response('Item successfully deleted!')
