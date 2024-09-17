from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = Categoria.objects.filter(parent__isnull=True)

    def clean_parent(self):
        parent = self.cleaned_data['parent']
        if parent and parent.parent:
            raise forms.ValidationError("Escoja una categoría válida.")
        return parent

    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'parent']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
        }
