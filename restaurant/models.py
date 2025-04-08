from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField(validators=[MaxValueValidator(6)])
    booking_date = models.DateTimeField(
        verbose_name="Booking Date and Time",
        default=timezone.now,
        db_index=True
    )

    def __str__(self):
        return self.name

class Menu(models.Model):
    title =models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
