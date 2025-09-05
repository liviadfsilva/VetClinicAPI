from django.db import models

class User(models.Model):
    class RoleType(models.TextChoices):
        ADMIN = "admin", "Admin"
        RECEPTIONIST = "receptionist", "Receptionist"
        STAFF = "staff", "Staff"
        VET = "vet", "Vet"
    
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=50, choices=RoleType.choices, default=RoleType.STAFF)
    
    class Meta:
        db_table = "users"