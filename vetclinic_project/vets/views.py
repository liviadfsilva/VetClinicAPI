from rest_framework import viewsets
from .models import Vets
from .serializer import VetsSerializer
from rest_framework.permissions import IsAuthenticated

class VetsViewSet(viewsets.ModelViewSet):
    queryset = Vets.objects.all()
    serializer_class = VetsSerializer
    permission_classes = [IsAuthenticated]