from rest_framework import viewsets
from .models import Pet
from .serializer import PetSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action
from rest_framework.response import Response

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=["get"], url_path="by-type")
    def by_type(self, request):
        type_param = request.query_params.get("type")
        
        if not type_param:
            return Response({"error": "Type parameter is required"}, status=400)
        
        pets = Pet.objects.filter(animal_type=type_param)
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)