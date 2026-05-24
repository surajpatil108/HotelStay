
# catalog/views.py
from django.shortcuts import render
from .models import RoomCategory

def home(request):
    # Fetch all room categories from the database
    categories = RoomCategory.objects.all()
    return render(request, 'catalog/home.html', {'categories': categories})

def contact_us(request):
    return render(request, 'catalog/contact.html')