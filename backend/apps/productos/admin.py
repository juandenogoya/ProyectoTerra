"""
Configuración del admin para los modelos de Productos.
"""

from django.contrib import admin
from .models import Categoria, Talla, Color, Producto, ProductoVariante


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Admin para Categoría.
    """
    list_display = ['nombre', 'padre', 'orden', 'is_active']
    list_filter = ['is_active', 'padre']
    search_fields = ['nombre']
    ordering = ['orden', 'nombre']


@admin.register(Talla)
class TallaAdmin(admin.ModelAdmin):
    """
    Admin para Talla.
    """
    list_display = ['nombre', 'orden', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nombre']
    ordering = ['orden']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """
    Admin para Color.
    """
    list_display = ['nombre', 'codigo_hex', 'is_active']
    list_filter = ['is_active']
    search_fields = ['nombre']
    ordering = ['nombre']


class ProductoVarianteInline(admin.TabularInline):
    """
    Inline para variantes de producto.
    """
    model = ProductoVariante
    extra = 0
    fields = ['talla', 'color', 'stock', 'sku']
    readonly_fields = ['sku']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    Admin para Producto.
    """
    list_display = [
        'codigo',
        'nombre',
        'categoria',
        'precio_venta',
        'stock_total',
        'is_active',
        'created_at'
    ]
    list_filter = [
        'categoria',
        'en_promocion',
        'tiene_variantes',
        'is_active',
        'created_at'
    ]
    search_fields = [
        'codigo',
        'nombre',
        'codigo_barras'
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
        'created_by',
        'updated_by'
    ]
    inlines = [ProductoVarianteInline]

    fieldsets = (
        ('Información Básica', {
            'fields': (
                'codigo',
                'nombre',
                'descripcion',
                'categoria',
                'proveedor'
            )
        }),
        ('Precios', {
            'fields': (
                'precio_costo',
                'precio_venta',
                'precio_promocion',
                'en_promocion'
            )
        }),
        ('Stock', {
            'fields': (
                'stock_minimo',
                'tiene_variantes'
            )
        }),
        ('Códigos', {
            'fields': (
                'codigo_barras',
            )
        }),
        ('Imagen', {
            'fields': ('imagen',)
        }),
        ('Estado', {
            'fields': ('is_active',)
        }),
        ('Auditoría', {
            'fields': (
                'created_at',
                'updated_at',
                'created_by',
                'updated_by'
            ),
            'classes': ('collapse',)
        })
    )


@admin.register(ProductoVariante)
class ProductoVarianteAdmin(admin.ModelAdmin):
    """
    Admin para ProductoVariante.
    """
    list_display = [
        'sku',
        'producto',
        'talla',
        'color',
        'stock',
        'is_active'
    ]
    list_filter = [
        'talla',
        'color',
        'is_active'
    ]
    search_fields = [
        'sku',
        'producto__nombre',
        'producto__codigo'
    ]
    readonly_fields = ['sku', 'created_at', 'updated_at']
