from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def home(request): #aqui empiezan las rutas como el index
    return render(request, 'home.html')    
    
def login(request): 
    
        if request.method == 'GET':
            return render(request, 'login.html',{ 
            'form': UserCreationForm
    })    
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(username=request.POST['username'],
                    password=request.POST['password1']) #captura los datos y los guardan 
                    user.save()
                    return HttpResponse('Usuario Created')
                except:
                    return render(request, 'login.html',{ 
            'form': UserCreationForm,
            'error': 'usuario ya creado'
    })  
            return render(request, 'login.html',{ 
            'form': UserCreationForm,
            'error': 'las contraseña no coinciden'  
            })  
                
            
            
            
        