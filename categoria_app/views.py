from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria
from .forms import CategoriaForm

# Create your views here.
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_app/categoria_lista.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        return Categoria.objects.filter(parent__isnull=True)

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_app/categoria_detalle.html'
    context_object_name = 'categoria'


@login_required
def categoria_crear(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')
    else:
        form = CategoriaForm()
    return render(request, 'categoria_app/categoria_crear.html', {'form': form})


@login_required
def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria_app/categoria_editar.html', {'form': form})