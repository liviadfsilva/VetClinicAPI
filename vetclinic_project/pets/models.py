from django.db import models

class Pet(models.Model):
    class AnimalType(models.TextChoices):
        BIRD = "bird", "Bird"
        CAT = "cat", "Cat"
        DOG = "dog", "Dog"
        FERRET = "ferret", "Ferret"
        RABBIT = "rabbit", "Rabbit"   
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    animal_type = models.CharField(max_length=50, choices=AnimalType.choices, default=AnimalType.CAT)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default="unknown")
    sex = models.CharField(max_length=1)
    neutered_spayed = models.CharField(max_length=1)
    
    def __str__(self):
        return f"{self.name} ({self.get_animal_type_display()})"
    
    class Meta:
        db_table = "pets"