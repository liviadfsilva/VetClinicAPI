from rest_framework import serializers
from .models import Pet
from appointments.serializer import AppointmentSerializer

class PetSerializer(serializers.ModelSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pet
        fields = ["id", "name", "age", "animal_type", "breed", "color", "sex", "neutered_spayed"]