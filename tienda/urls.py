"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'), #index
    
    path('login/', views.login, name='login'),#son las rutas
    
    path('Registro/', views.RegistrosUsuarios, name='RegistroUsuario'),
    
    path('Carrito/', views.CarritoCompra, name='Carrito'),
    
    path('Catalogo/', views.CatalogoProducto, name='CatalogoProductos'),
    
    path('Detalle/', views.ProductoDetalle, name='DetalleProducto'),
    
    path('Dashboard/', views.Dashboard, name='Dashboard'),    
    
    path('GestionCompra/', views.GestionCompra, name='GestionCompra'),
    
    path('GestionVenta/', views.GestionVenta, name='GestionVenta'),
    
    path('GenerarPedido/', views.GenerarPedido, name='GenerarPedido'),
    
    path('PedidoRealizado/', views.PedidoRealizado, name='PedidoRealizado'),
    
    path('Proveedores/', views.Proveedores, name='Proveedores'),
    
    path('Recuperacion/', views.RecuperacionContraseña, name='RecuperacionContraseña'),
    
    path('Roles/', views.Roles, name='Roles'),

    path('VentasRealizadas/', views.VentasRealizadas, name='VentasRealizadas'),
    
    
    
]

