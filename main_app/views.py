from django.shortcuts import render

cymbals = [
    {'type': 'crash', 'size' : 16, 'brand': 'Zildjian', 'description': 'Light', 'sale':'sold'},
    {'type': 'crash', 'size' : 18, 'brand': 'Sabian', 'description': 'Medium heavy', 'sale':'sold'},
    {'type': 'crash', 'size' : 17, 'brand': 'Ufip', 'description': 'Medium', 'sale':''},
    {'type': 'ride', 'size' : 21, 'brand': 'Zildjian', 'description': 'Washy', 'sale':'sold'},
    {'type': 'ride', 'size' : 20, 'brand': 'Sabian', 'description': 'Light', 'sale':''},
    {'type': 'ride', 'size' : 24, 'brand': 'Ufip', 'description': 'Pingy', 'sale':''},
    
    ]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html', {
        'cymbals': cymbals
    })
