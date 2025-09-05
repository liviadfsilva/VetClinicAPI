from rest_framework import serializers
from .models import Vets
from appointments.serializer import AppointmentSerializer

class VetsSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Vets
        fields = ["name", "date_of_birth", "email", "phone"]