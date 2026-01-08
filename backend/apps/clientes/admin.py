"""
Configuración del admin para el modelo Cliente.
"""

from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Configuración del admin para Cliente.
    """
    list_display = [
        'numero_documento',
        'nombre_completo',
        'email',
        'telefono',
        'tipo_cliente',
        'saldo_actual',
        'is_active',
        'created_at'
    ]
    list_filter = [
        'tipo_cliente',
        'tipo_documento',
        'is_active',
        'provincia',
        'created_at'
    ]
    search_fields = [
        'numero_documento',
        'nombre',
        'apellido',
        'email',
        'telefono'
    ]
    readonly_fields = [
        'created_at',
        'updated_at',
        'created_by',
        'updated_by',
        'saldo_actual'
    ]

    fieldsets = (
        ('Información Personal', {
            'fields': (
                'tipo_documento',
                'numero_documento',
                'nombre',
                'apellido',
                'email',
                'telefono',
                'fecha_nacimiento'
            )
        }),
        ('Dirección', {
            'fields': (
                'calle',
                'numero',
                'piso',
                'departamento',
                'localidad',
                'provincia',
                'codigo_postal',
                'pais'
            )
        }),
        ('Información Comercial', {
            'fields': (
                'tipo_cliente',
                'limite_credito',
                'saldo_actual',
                'descuento_porcentaje'
            )
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

    def nombre_completo(self, obj):
        return obj.nombre_completo
    nombre_completo.short_description = 'Nombre Completo'
