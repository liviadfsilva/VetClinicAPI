from rest_framework import serializers
from .models import Appointments

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ["pet", "vet", "owner", "date", "time", "type", "notes", "amount", "payment_method", "payment_status"]