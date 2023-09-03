from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request): #aqui empiezan las rutas como el index
    return render(request, 'home.html')    
    
def login(request): 
    return render(request, 'login.html',{ 
        'form': UserCreationForm
    })    