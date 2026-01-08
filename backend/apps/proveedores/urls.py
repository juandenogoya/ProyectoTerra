"""
URLs para la app de proveedores.
"""

from django.urls import path
from . import views

app_name = 'proveedores'

urlpatterns = [
    path('', views.listar_proveedores, name='listar'),
    path('nuevo/', views.crear_proveedor, name='crear'),
    path('<int:pk>/', views.ver_proveedor, name='ver'),
    path('<int:pk>/editar/', views.editar_proveedor, name='editar'),
]
