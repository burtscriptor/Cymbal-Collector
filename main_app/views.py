from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Cymbal

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    cymbal = Cymbal.objects.all()
    return render(request, 'index.html', {
        'cymbal': cymbal
    })

def details(request, cymbal_id):
    cymbal = Cymbal.objects.get(id=cymbal_id)
    return render(request, 'details.html', { "cymbal": cymbal })

class CreateCymbal(CreateView):
    model = Cymbal
    fields = '__all__'
    
class CymbalDelete(DeleteView):
    model = Cymbal
    success_url = '/cymbals/'

class CymbalUpdate(UpdateView):
    model = Cymbal
    fields = ['size', 'description', 'brand']