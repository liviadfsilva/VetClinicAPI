from rest_framework import viewsets
from .models import Owner
from .serializer import OwnerSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer