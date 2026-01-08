"""
Vistas para la gestión de productos.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Producto, ProductoVariante
from .forms import ProductoForm


@login_required
def listar_productos(request):
    """Lista todos los productos activos con búsqueda."""
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(is_active=True).select_related('categoria', 'proveedor')

    if query:
        productos = productos.filter(
            Q(codigo__icontains=query) |
            Q(nombre__icontains=query) |
            Q(codigo_barras__icontains=query)
        )

    productos = productos.order_by('-created_at')

    context = {
        'title': 'Productos',
        'productos': productos,
        'query': query
    }
    return render(request, 'productos/listar.html', context)


@login_required
def crear_producto(request):
    """Crea un nuevo producto."""
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.created_by = request.user
            producto.save()
            messages.success(request, f'Producto {producto.nombre} creado exitosamente.')
            return redirect('productos:listar')
    else:
        form = ProductoForm()

    context = {
        'title': 'Nuevo Producto',
        'form': form
    }
    return render(request, 'productos/form.html', context)


@login_required
def ver_producto(request, pk):
    """Muestra los detalles de un producto."""
    producto = get_object_or_404(Producto, pk=pk, is_active=True)
    variantes = producto.variantes.select_related('talla', 'color').filter(is_active=True)

    context = {
        'title': f'Producto: {producto.nombre}',
        'producto': producto,
        'variantes': variantes
    }
    return render(request, 'productos/detalle.html', context)
