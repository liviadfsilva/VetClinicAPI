from rest_framework import viewsets
from .models import Vets
from .serializer import VetsSerializer

class VetsViewSet(viewsets.ModelViewSet):
    queryset = Vets.objects.all()
    serializer_class = VetsSerializer