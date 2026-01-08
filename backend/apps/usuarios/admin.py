"""
Configuración del admin para el modelo Usuario.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    """
    Configuración personalizada del admin para Usuario.
    """
    list_display = ['username', 'email', 'first_name', 'last_name', 'rol', 'is_active', 'created_at']
    list_filter = ['rol', 'is_active', 'is_staff', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información Adicional', {
            'fields': ('rol', 'telefono', 'direccion', 'foto')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    readonly_fields = ['created_at', 'updated_at']

    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Información Adicional', {
            'fields': ('rol', 'telefono', 'email')
        }),
    )
