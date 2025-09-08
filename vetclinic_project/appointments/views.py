from rest_framework import viewsets
from .models import Appointments
from .serializer import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]