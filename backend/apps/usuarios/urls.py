"""
URLs de la app usuarios.
"""

from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
]
