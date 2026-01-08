"""
URLs para la app de productos.
"""

from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.listar_productos, name='listar'),
    path('nuevo/', views.crear_producto, name='crear'),
    path('<int:pk>/', views.ver_producto, name='ver'),
]
