from django.db import models
from pets.models import Pet
from vets.models import Vets
from owners.models import Owner
from datetime import time

class Appointments(models.Model):
    class AppointmentType(models.TextChoices):
        CHECK_UP = "check_up", "Check-up"
        EMERGENCY = "emergency", "Emergency"
        SURGERY = "surgery", "Surgery"
        VACCINATION = "vaccination", "Vaccination"
        GROOMING = "grooming", "Grooming"
        FOLLOW_UP = "follow_up", "Follow-up"
        
    class PaymentStatus(models.TextChoices):
        APPROVED = "approved", "Approved"
        PENDING = "pending", "Pending"
        CANCELED = "canceled", "Canceled"
        FAILED = "failed", "Failed"
        REFUND = "refund", "Refund"
        
    
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments", default=500)
    vet = models.ForeignKey(Vets, on_delete=models.CASCADE, related_name="appointments", default=500)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="appointments", default=500)
    date = models.DateField()
    time = models.TimeField(default=time(0, 9))
    type = models.CharField(max_length=100, choices=AppointmentType.choices, default=AppointmentType.CHECK_UP)
    notes = models.CharField(max_length=500)
    amount = models.CharField(max_length=100, null=True)
    payment_method = models.CharField(max_length=100, null=True)
    payment_status = models.CharField(max_length=100, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    
    class Meta:
        db_table = "appointments"