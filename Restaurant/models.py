from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    description = models.TextField(max_length=1000, default="")

    def __str__(self):
        return f"{self.name}: ${self.price}"


class Booking(models.Model):
    name = models.CharField(max_length=50)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}: {self.booking_date}"
