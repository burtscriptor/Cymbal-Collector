from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import DetailView, ListView
from .models import Cymbal, Artist
from .forms import HireForm
from django.urls import reverse

#Cymbal
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
    current_artist_ids = cymbal.artist.all().values_list('id')
    available_artist = Artist.objects.exclude(id__in=current_artist_ids)
    return render(request, 'details.html', { "cymbal": cymbal, 
                                            'hire_form': hire_form,
                                             'available_artist': available_artist,
                                              })


def add_hire(request, cymbal_id):
    hire_form = HireForm(request.POST)
    if hire_form.is_valid():
        new_hire = hire_form.save(commit=False)
        new_hire.cymbal_id = cymbal_id
        new_hire.save()
    return redirect('details', cymbal_id=cymbal_id)    

class CreateCymbals(CreateView):
    model = Cymbal
    fields = ['type', 'size', 'brand', 'description', 'series']
    
class CymbalDelete(DeleteView):
    model = Cymbal
    success_url = '/cymbals/'

class CymbalUpdate(UpdateView):
    model = Cymbal
    fields = ['size', 'description', 'brand', 'series']

#Artist
class IndexArtist(ListView):
    model = Artist

class CreateArtist(CreateView):
    model = Artist    
    fields = '__all__'

class Artists_Detail(DetailView):
    model = Artist    

class UpdateArtist(UpdateView):
    model = Artist
    fields = '__all__'

class DeleteArtist(DeleteView):
    model = Artist
    success_url = '/artist/'

def add_artist(request, cymbal_id, artist_id):
    Cymbal.objects.get(id=cymbal_id).artist.add(artist_id)
    return redirect('details', cymbal_id=cymbal_id)

def remove_artist(request, cymbal_id, artist_id):
    Cymbal.objects.get(id=cymbal_id).artist.remove(artist_id)
    return redirect('details', cymbal_id=cymbal_id)