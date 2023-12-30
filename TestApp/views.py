from django.shortcuts import render

# Create your views here.
from .models import City, Section, Street, Apartment

def city_view(request):
    cities = City.objects.all()
    return render(request, 'city.html', {'cities': cities})

def section_view(request, city_id, section_id):
    sections = Section.objects.filter(city_id=city_id)
    streets = Street.objects.filter(section_id=section_id)
    return render(request, 'section.html', {'sections': sections, 'streets': streets})

def street_view(request, street_id):
    apartments = Apartment.objects.filter(street_id=street_id)
    return render(request, 'street.html', {'apartments': apartments})
