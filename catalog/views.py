
# catalog/views.py
from django.shortcuts import render, redirect
from .models import RoomCategory, Testimonial


def home(request):
    # Simplifed home view: just fetches data to display
    categories = RoomCategory.objects.all()
    testimonials = Testimonial.objects.all().order_by('-created_at') 

    context = {
        'categories': categories,
        'testimonials': testimonials,
    }
    return render(request, 'catalog/home.html', context)

# NEW VIEW: Handles rendering the form page AND saving the submission
def add_testimonial(request):
    if request.method == 'POST':
        guest_name = request.POST.get('name')
        location = request.POST.get('location')
        room_type = request.POST.get('room_type')
        quote = request.POST.get('review')

        if guest_name and quote:
            Testimonial.objects.create(
                guest_name=guest_name,
                location=location,
                room_type=room_type,
                quote=quote
            )
        return redirect('home') # Sends them back to the homepage to see their review!

    return render(request, 'catalog/add_review.html')

def contact_us(request):
    return render(request, 'catalog/contact.html')
