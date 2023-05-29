from django.test import TestCase

from .models import Booking, MenuItem


# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(name="IceCream", price=80, inventory=100, description="Vanilla")
        self.assertEqual(str(item), "IceCream: $80")


class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="John", no_of_guests=100, booking_date="2023-05-30", comment="OK")
        self.assertEqual(str(item), "John: 2023-05-30")
