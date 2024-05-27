from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', pagina_inicio, name='pagina_inicio'),
    path('listar_clientes/', listar_clientes, name='listar_clientes'),
    path('crear_cliente/', crear_cliente, name='crear_cliente'),

]