from django.db import models
from pets.models import Pet
from vets.models import Vets

class Appointments(models.Model):
    class AppointmentType(models.TextChoices):
        CHECK_UP = "check_up", "Check-up"
        EMERGENCY = "emergency", "Emergency"
        SURGERY = "surgery", "Surgery"
        VACCINATION = "vaccination", "Vaccination"
        GROOMING = "grooming", "Grooming"
        FOLLOW_UP = "follow_up", "Follow-up"
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments", default=500)
    vet = models.ForeignKey(Vets, on_delete=models.CASCADE, related_name="appointments", default=500)
    date = models.DateTimeField()
    type = models.CharField(max_length=100, choices=AppointmentType.choices, default=AppointmentType.CHECK_UP)
    notes = models.CharField(max_length=500)
    
    class Meta:
        db_table = "appointments"