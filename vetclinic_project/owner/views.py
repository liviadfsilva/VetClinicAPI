from rest_framework import viewsets
from .models import Owner
from .serializer import OwnerSerializer
from rest_framework.permissions import IsAuthenticated

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]