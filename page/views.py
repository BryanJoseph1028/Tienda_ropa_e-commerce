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

def CarritoCompras(request): 
    return render(request, 'CarritoCompras.html')    

def CatalogoProducto(request): 
    return render(request, 'CatalogoProductos.html')  

def Compra(request): 
    return render(request, 'Compra.html')

def GestionCompra(request): 
    return render(request, 'GestionCompra.html')

def Dashboard(request): 
    return render(request, 'Dashboard.html')

def GestionVenta(request): 
    return render(request, 'GestionVenta.html')      

def GenerarPedido(request): 
    return render(request, 'GenerarPedido.html')   

def ProductoDetalle(request): 
    return render(request, 'ProductoDetalle.html')  

def Proveedores(request): 
    return render(request, 'Proveedores.html')

def PedidoRealizado(request): 
    return render(request, 'PedidoRealizado.html')

def RecuperacionContraseña(request): 
    return render(request, 'Recuperacion.html')    

def RegistrosUsuarios(request): 
    return render(request, 'RegistrosUsuarios.html')

def Roles(request): 
    return render(request, 'Roles.html')

def VentasRealizadas(request): 
    return render(request, 'VentasRealizadas.html')     
            
            
        