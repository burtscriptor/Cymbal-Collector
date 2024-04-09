from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Cymbal
from .forms import HireForm
from django.urls import reverse

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
    hire_form = HireForm()
    return render(request, 'details.html', { "cymbal": cymbal, 'hire_form': hire_form })


def add_hire(request, cymbal_id):
    hire_form = HireForm(request.POST)
    if hire_form.is_valid():
        new_hire = hire_form.save(commit=False)
        new_hire.cymbal_id = cymbal_id
        new_hire.save()
    return redirect('details', cymbal_id=cymbal_id)    

class CreateCymbal(CreateView):
    model = Cymbal
    fields = '__all__'
    
class CymbalDelete(DeleteView):
    model = Cymbal
    success_url = '/cymbals/'

class CymbalUpdate(UpdateView):
    model = Cymbal
    fields = ['size', 'description', 'brand']