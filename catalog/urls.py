# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_us, name='contact'),
    path('add-review/', views.add_testimonial, name='add_testimonial'),
]