from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Etiqueta
from .forms import EtiquetaForm

# Create your views here.
class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'etiquetas_app/etiqueta_lista.html'
    context_object_name = 'etiquetas'

class EtiquetaDetailView(DetailView):
    model = Etiqueta
    template_name = 'etiquetas_app/etiqueta_detalle.html'
    context_object_name = 'etiqueta'

def etiqueta_crear(request):
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm()
    return render(request, 'etiquetas_app/etiqueta_crear.html', {'form': form})

def etiqueta_editar(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == "POST":
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('etiqueta_list')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiquetas_app/etiqueta_editar.html', {'form': form})



    