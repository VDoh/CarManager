from django.db import models
from django.core.validators import RegexValidator


CAR_CATEGORY_CHOICES = (
    ("First Class", "First Class"),
    ("Bizness Class", "Bizness Class"),
    ("Economic Class", "Economic Class")
)

ENGINE_TYPE_CHOICES = (
    ("Electric", "Electric"),
    ("Normal", "Normal"),
    ("Hybrid", "Hybrid")
)

class Car(models.Model):
    
    registerPlate = models.CharField(max_length=25, validators=[RegexValidator(regex='^[A-Z0-9]+$', 
        message="Wrong Plate number format, there cannot be lowercase letters and special chars")], unique=True)
    maxPassengerAllowed = models.PositiveIntegerField()
    productionDate = models.DateField()
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=25)
    carCategory = models.CharField(max_length=17, choices=CAR_CATEGORY_CHOICES, default="Economic Class")
    engineType = models.CharField(max_length=8, choices=ENGINE_TYPE_CHOICES, default="Normal")

    
    def __str__(self):
      return self.registerPlate


