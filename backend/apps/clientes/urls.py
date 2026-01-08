"""
URLs para la app de clientes.
"""

from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.listar_clientes, name='listar'),
    path('nuevo/', views.crear_cliente, name='crear'),
    path('<int:pk>/', views.ver_cliente, name='ver'),
    path('<int:pk>/editar/', views.editar_cliente, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_cliente, name='eliminar'),
]
