"""
Vistas para autenticación y gestión de usuarios.
"""

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm


def user_login(request):
    """
    Vista de login.
    """
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.get_full_name() or user.username}!')
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    context = {
        'form': form,
        'title': 'Iniciar Sesión'
    }
    return render(request, 'usuarios/login.html', context)


@login_required
def user_logout(request):
    """
    Vista de logout.
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('usuarios:login')


@login_required
def perfil(request):
    """
    Vista de perfil de usuario.
    """
    context = {
        'title': 'Mi Perfil',
        'usuario': request.user
    }
    return render(request, 'usuarios/perfil.html', context)
