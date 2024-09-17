from django import forms
from .models import Etiqueta

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre', 'productos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }