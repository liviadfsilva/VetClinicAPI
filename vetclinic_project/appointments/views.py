from rest_framework import viewsets
from .models import Appointments
from .serializer import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentSerializer