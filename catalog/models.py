# catalog/models.py
from django.db import models


class RoomCategory(models.Model):
    ROOM_TYPES = [
        ('AC', 'AC Room'),
        ('NON_AC', 'Non-AC Room'),
        ('DELUXE', 'Deluxe Suite'),
        ('LUXURY', 'Luxury Premium'),
    ]

    name = models.CharField(max_length=100, choices=ROOM_TYPES, unique=True)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    # image = models.ImageField(upload_file='room_images/')
    image = models.ImageField(upload_to="room_images/", blank=True, null=True)

    capacity = models.IntegerField(default=2) # e.g., 2 Guests

    def __str__(self):
        return self.get_name_display()