"""
Formularios para autenticación y gestión de usuarios.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario


class LoginForm(AuthenticationForm):
    """
    Formulario de login personalizado.
    """
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ingrese su usuario',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ingrese su contraseña'
        })
    )


class UsuarioCreationForm(UserCreationForm):
    """
    Formulario para crear nuevos usuarios.
    """
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'rol', 'telefono']
