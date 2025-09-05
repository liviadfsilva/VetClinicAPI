from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "owners"