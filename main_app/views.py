from django.shortcuts import render
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