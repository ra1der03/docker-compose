from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

#
# @api_view(['GET'])
# def get_animals(request):
#     animals = Animal.objects.all()
#     serializer = AnimalSerializer(animals, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_animal(request, pk):
#     animal = Animal.objects.get(id=pk)
#     serializer = AnimalSerializer(animal, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def add_animal(request):
#     serializer = AnimalSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['PUT'])
# def update_animal(request, pk):
#     animal = Animal.objects.get(id=pk)
#     serializer = AnimalSerializer.update(Animal.objects[pk], instance=animal, data=request.data)
#     serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def delete_animal(request, pk):
#     animal = Animal.objects.get(id=pk)
#     animal.delete()
#     return Response('Item successfully deleted!')
