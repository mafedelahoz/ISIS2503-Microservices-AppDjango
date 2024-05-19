from django.shortcuts import render
from django.http import JsonResponse
from .models import Place

def create_place(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        place = Place(name=name, description=description)
        place.save()
        return JsonResponse({'message': 'Place created successfully'})

def list_places(request):
    places = Place.objects.all()
    return JsonResponse({'places': list(places.values())})
