from rest_framework import serializers
from .models import Owner

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "name", "date_of_birth", "email", "phone", "address", "city", "zip", "state"]