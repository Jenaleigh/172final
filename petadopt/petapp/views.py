from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'petapp/index.html')

def pets(request):
    type_list=Pet.objects.all()
    return render(request, 'petapp/pets.html', {'type_list': type_list})

