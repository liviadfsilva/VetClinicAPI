from rest_framework import viewsets
from .models import Pet
from .serializer import PetSerializer
from rest_framework.permissions import IsAuthenticated

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]