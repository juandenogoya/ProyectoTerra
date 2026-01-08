"""
Vistas para la gestión de clientes.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Cliente
from .forms import ClienteForm


@login_required
def listar_clientes(request):
    """Lista todos los clientes activos con búsqueda."""
    query = request.GET.get('q', '')
    clientes = Cliente.objects.filter(is_active=True)

    if query:
        clientes = clientes.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(numero_documento__icontains=query) |
            Q(email__icontains=query)
        )

    clientes = clientes.order_by('-created_at')

    context = {
        'title': 'Clientes',
        'clientes': clientes,
        'query': query
    }
    return render(request, 'clientes/listar.html', context)


@login_required
def crear_cliente(request):
    """Crea un nuevo cliente."""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.created_by = request.user
            cliente.save()
            messages.success(request, f'Cliente {cliente.nombre_completo} creado exitosamente.')
            return redirect('clientes:listar')
    else:
        form = ClienteForm()

    context = {
        'title': 'Nuevo Cliente',
        'form': form
    }
    return render(request, 'clientes/form.html', context)


@login_required
def editar_cliente(request, pk):
    """Edita un cliente existente."""
    cliente = get_object_or_404(Cliente, pk=pk, is_active=True)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.updated_by = request.user
            cliente.save()
            messages.success(request, f'Cliente {cliente.nombre_completo} actualizado exitosamente.')
            return redirect('clientes:listar')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'title': 'Editar Cliente',
        'form': form,
        'cliente': cliente
    }
    return render(request, 'clientes/form.html', context)


@login_required
def ver_cliente(request, pk):
    """Muestra los detalles de un cliente."""
    cliente = get_object_or_404(Cliente, pk=pk, is_active=True)

    context = {
        'title': f'Cliente: {cliente.nombre_completo}',
        'cliente': cliente
    }
    return render(request, 'clientes/detalle.html', context)


@login_required
def eliminar_cliente(request, pk):
    """Elimina (soft delete) un cliente."""
    cliente = get_object_or_404(Cliente, pk=pk, is_active=True)

    if request.method == 'POST':
        cliente.soft_delete()
        messages.success(request, f'Cliente {cliente.nombre_completo} eliminado.')
        return redirect('clientes:listar')

    context = {
        'title': 'Eliminar Cliente',
        'cliente': cliente
    }
    return render(request, 'clientes/eliminar.html', context)
