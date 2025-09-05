from django.db import models

class Vets(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100, unique=True)
    
    class Meta:
        db_table = "vets"