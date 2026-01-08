"""
Configuración del admin para el modelo Proveedor.
"""

from django.contrib import admin
from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    """
    Configuración del admin para Proveedor.
    """
    list_display = [
        'nombre_display',
        'cuit',
        'tipo_proveedor',
        'email',
        'telefono',
        'is_active',
        'created_at'
    ]
    list_filter = [
        'tipo_proveedor',
        'is_active',
        'provincia',
        'created_at'
    ]
    search_fields = [
        'razon_social',
        'nombre_fantasia',
        'cuit',
        'email'
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
        'created_by',
        'updated_by'
    ]

    fieldsets = (
        ('Información de la Empresa', {
            'fields': (
                'razon_social',
                'nombre_fantasia',
                'cuit',
                'tipo_proveedor'
            )
        }),
        ('Contacto Principal', {
            'fields': (
                'email',
                'telefono',
                'sitio_web'
            )
        }),
        ('Dirección', {
            'fields': (
                'calle',
                'numero',
                'piso',
                'localidad',
                'provincia',
                'codigo_postal',
                'pais'
            )
        }),
        ('Información Comercial', {
            'fields': (
                'condiciones_pago',
                'descuento_pronto_pago',
                'plazo_entrega_dias'
            )
        }),
        ('Contacto Adicional', {
            'fields': (
                'contacto_nombre',
                'contacto_telefono',
                'contacto_email'
            ),
            'classes': ('collapse',)
        }),
        ('Notas', {
            'fields': ('notas',)
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

    def nombre_display(self, obj):
        return obj.nombre_display
    nombre_display.short_description = 'Nombre'
