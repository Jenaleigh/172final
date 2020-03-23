from django.shortcuts import render
from .models import Pet
# Create your views here.

def index(request):
    return render(request, 'petapp/index.html')

def pets(request):
    try:
        pet=Pet.objects.all()
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'petapp/pets.html', {'pet': pet})

