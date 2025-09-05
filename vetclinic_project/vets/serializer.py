from rest_framework import serializers
from .models import Vets

class VetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vets
        fields = ["name", "date_of_birth", "email", "phone"]