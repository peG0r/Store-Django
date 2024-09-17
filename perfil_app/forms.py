from .models import Perfil, User
from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre_completo', 'fecha_nacimiento', 'direccion', 'telefono', 'descripcion', 'avatar', 'rol']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }