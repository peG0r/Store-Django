from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from .models import Producto
from .forms import ProductoForm

# Create your views here.




class ProductoListView(ListView):
    model = Producto
    template_name = 'productos_app/producto_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos_app/producto_detail.html'
    context_object_name = 'producto'

@login_required
def producto_create(request):
    if request.user.perfil.rol != 'VE':
        return render(request, 'acceso_denegado.html')  # Ajusta esto según tus necesidades

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    
    return render(request, 'productos_app/producto_create.html', {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos_app/producto_edit.html', {'form': form}, )

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'productos_app/producto_delete.html', {'producto': producto})


