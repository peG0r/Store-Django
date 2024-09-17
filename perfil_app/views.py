from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db import IntegrityError, transaction
from .forms import PerfilForm, UserForm
from .models import Perfil

# Create your views here.
User = get_user_model()

def perfil_detalle(request, user_id):
    perfil = get_object_or_404(Perfil, usuario_id=user_id)
    es_autenticado = request.user.is_authenticated

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_detalle', user_id=perfil.usuario.id)
    else:
        form = PerfilForm(instance=perfil)
    
    context = {
        'user': request.user,
        'perfil': perfil,
        'form': form,
        'es_autenticado': es_autenticado
    }
    
    return render(request, 'perfil_app/perfil_detalle.html', context)

def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            try:
                with transaction.atomic():
                    user = user_form.save(commit=False)
                    user.set_password(user_form.cleaned_data['password1'])  # Hash the password
                    user.save()
                    
                    # Verificar si el perfil ya existe
                    if not Perfil.objects.filter(usuario=user).exists():
                        Perfil.objects.create(usuario=user)  # Crear perfil vacío
                    login(request, user)  # Log in the user after creation
                    return redirect('perfil_detalle', user_id=user.id)
            except IntegrityError as e:
                messages.error(request, f'Error al crear el perfil: {e}')
                print(f'Error al crear el perfil: {e}')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
            print(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request, 'perfil_app/user_form.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')  # Redirect to a homepage or any other page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'perfil_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def acceso_denegado(request):
    return render(request, 'acceso_denegado.html')