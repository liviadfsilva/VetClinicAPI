from rest_framework import serializers
from .models import Owner
from pets.serializer import PetSerializer

class OwnerSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)
    
    class Meta:
        model = Owner
        fields = ["id", "name", "date_of_birth", "email", "phone", "address", "city", "zip", "state", "pets"]