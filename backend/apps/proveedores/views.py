"""
Vistas para la gestión de proveedores.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Proveedor
from .forms import ProveedorForm


@login_required
def listar_proveedores(request):
    """Lista todos los proveedores activos con búsqueda."""
    query = request.GET.get('q', '')
    proveedores = Proveedor.objects.filter(is_active=True)

    if query:
        proveedores = proveedores.filter(
            Q(razon_social__icontains=query) |
            Q(nombre_fantasia__icontains=query) |
            Q(cuit__icontains=query)
        )

    proveedores = proveedores.order_by('razon_social')

    context = {
        'title': 'Proveedores',
        'proveedores': proveedores,
        'query': query
    }
    return render(request, 'proveedores/listar.html', context)


@login_required
def crear_proveedor(request):
    """Crea un nuevo proveedor."""
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            proveedor = form.save(commit=False)
            proveedor.created_by = request.user
            proveedor.save()
            messages.success(request, f'Proveedor {proveedor.nombre_display} creado exitosamente.')
            return redirect('proveedores:listar')
    else:
        form = ProveedorForm()

    context = {
        'title': 'Nuevo Proveedor',
        'form': form
    }
    return render(request, 'proveedores/form.html', context)


@login_required
def editar_proveedor(request, pk):
    """Edita un proveedor existente."""
    proveedor = get_object_or_404(Proveedor, pk=pk, is_active=True)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            proveedor = form.save(commit=False)
            proveedor.updated_by = request.user
            proveedor.save()
            messages.success(request, f'Proveedor {proveedor.nombre_display} actualizado.')
            return redirect('proveedores:listar')
    else:
        form = ProveedorForm(instance=proveedor)

    context = {
        'title': 'Editar Proveedor',
        'form': form,
        'proveedor': proveedor
    }
    return render(request, 'proveedores/form.html', context)


@login_required
def ver_proveedor(request, pk):
    """Muestra los detalles de un proveedor."""
    proveedor = get_object_or_404(Proveedor, pk=pk, is_active=True)

    context = {
        'title': f'Proveedor: {proveedor.nombre_display}',
        'proveedor': proveedor
    }
    return render(request, 'proveedores/detalle.html', context)
