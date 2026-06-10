from django.contrib import admin
from .models import RoomCategory, RoomImage, Testimonial

# Register your models here.
# admin.site.register(RoomCategory)

# This allows editing gallery images directly inside the Room Category editor
class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 3 # Gives you 3 empty image upload slots by default

@admin.register(RoomCategory)
class RoomCategoryAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]


admin.site.register(Testimonial)