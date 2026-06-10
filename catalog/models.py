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
    image = models.ImageField(upload_to="room_images/", blank=True, null=True)

    capacity = models.IntegerField(default=2) # e.g., 2 Guests

    def __str__(self):
        return self.get_name_display()

# NEW MODEL: Supports unlimited secondary images
class RoomImage(models.Model):
    # Links each image to a specific RoomCategory
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to="room_gallery/")
    caption = models.CharField(max_length=100, blank=True, help_text="Optional description for this photo")

    def __str__(self):
        return f"Gallery Photo for {self.room_category.get_name_display()}"


class Testimonial(models.Model):
    ROOM_TYPES = [
        ('AC', 'AC Room'),
        ('NON_AC', 'Non-AC Room'),
        ('DELUXE', 'Deluxe Suite'),
        ('LUXURY', 'Luxury Premium'),
    ]

    guest_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, help_text="e.g., New York, Mumbai")
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Quick fix to add a placeholder support dynamically via standard init
        self._meta.get_field('location').placeholder = "e.g., New York"

    def __str__(self):
        return f"Review by {self.guest_name}"