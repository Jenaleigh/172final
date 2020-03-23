from django.shortcuts import render
from .models import Pet
from django.contrib.auth.decorators import login_required
from .forms import PetForm
# Create your views here.

def index(request):
    return render(request, 'petapp/index.html')

def pets(request):
    try:
        pet=Pet.objects.all()
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'petapp/pets.html', {'pet': pet})

def loginmessage(request):
    return render(request, 'petapp/loginmessage.html')

def logoutmessage(request): 
    return render(request, 'petapp/logoutmessage.html')

@login_required
def newPet(request):
    form=PetForm
    if request.method=='POST':
        form=PetForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=PetForm()
    else:
        form=PetForm()
    return render(request, 'petapp/newpet.html', {'form': form})




