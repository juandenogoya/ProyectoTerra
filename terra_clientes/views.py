from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

# vista de inicio:
def pagina_inicio (request):
    return render (request, 'pagina_inicio.html')


# vista de ver clientes:
def listar_clientes (request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes}
    return render (request, 'listar_clientes.html', contexto)

# vista de alta de clientes:
def crear_cliente(request):
    if request.method == 'POST':
        form = AltaClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('listar_clientes')
    else:
        form = AltaClienteForm()

    contexto = {'form': form}
    return render(request, 'crear_cliente.html', contexto)



