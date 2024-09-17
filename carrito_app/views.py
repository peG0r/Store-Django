from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from productos_app.models import Producto
from .models import Carrito, CarritoItem
from django.contrib.sessions.models import Session
from django.db.models import Sum





User = get_user_model()

def ver_carrito(request):
    context = {}  
    return render(request, 'carrito_app/ver_carrito.html', context)

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.user.is_authenticated:
        # Si el usuario está autenticado, se asocia el carrito directamente al usuario
        usuario = request.user
        carrito, created = Carrito.objects.get_or_create(session=session)
    else:
        # Si el usuario no está autenticado, se utiliza la sesión para asociar el carrito
        session_key = request.session.session_key
        if session_key is None:
            request.session.save()
            session_key = request.session.session_key
        
        try:
            session = Session.objects.get(session_key=session_key)
        except Session.DoesNotExist:
            session = Session(session_key=session_key)
            session.save()
        
        # Crear o recuperar un carrito asociado a la sesión actual
        carrito, created = Carrito.objects.get_or_create(session=session)
    
    # Check if the product is already in the cart
    item = CarritoItem.objects.filter(carrito=carrito, producto=producto).first()
    if item:
        # If the product is already in the cart, increase the quantity
        item.cantidad += 1
        item.save()
    else:
        # If the product is not in the cart, add it with quantity 1
        CarritoItem.objects.create(carrito=carrito, producto=producto, cantidad=1)
        
    return redirect('ver_carrito')

def actualizar_cantidad(request, carrito_producto_id):
    carrito_producto = get_object_or_404(CarritoItem, id=carrito_producto_id)
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad'))
        if cantidad > 0:
            carrito_producto.cantidad = cantidad
            carrito_producto.save()
        else:
            carrito_producto.delete()
    return redirect('ver_carrito')

def eliminar_del_carrito(request, carrito_producto_id):
    carrito_producto = get_object_or_404(CarritoItem, id=carrito_producto_id)
    carrito_producto.delete()
    return redirect('ver_carrito')
