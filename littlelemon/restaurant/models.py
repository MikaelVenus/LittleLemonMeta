from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(999999)  # Maximum 6 digits
    ])
    booking_date = models.DateTimeField()

    def __str__(self):
            return self.name
    

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(99999)  # Maximum 6 digits
    ])

    def get_item(self): #Use for test
        return f'{self.title} : {str(self.price)}'
