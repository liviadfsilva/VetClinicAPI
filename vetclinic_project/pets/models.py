from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=10, default="unknown")
    sex = models.CharField(max_length=1)
    neutered_spayed = models.CharField(max_length=1)
    
    class Meta:
        db_table = "pets"