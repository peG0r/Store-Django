from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.all()
        self.fields['categoria'].widget = forms.Select(attrs={'class': 'form-control'}, choices=self.get_categorias_with_subcategorias())

    def get_categorias_with_subcategorias(self):
        categorias_with_subcategorias = []
        categorias = Categoria.objects.filter(parent__isnull=True)
        for categoria in categorias:
            subcategorias = categoria.subcategorias.all()
            if subcategorias:
                subcategoria_choices = [(subcategoria.id, f'{subcategoria.nombre} ({categoria.nombre})') for subcategoria in subcategorias]
                categorias_with_subcategorias.append((categoria.nombre, subcategoria_choices))
            else:
                categorias_with_subcategorias.append((categoria.nombre, [(categoria.id, categoria.nombre)]))
        return categorias_with_subcategorias

    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'descripcion', 'stock', 'imagen', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
