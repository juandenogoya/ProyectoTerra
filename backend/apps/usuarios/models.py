"""
Modelo de Usuario personalizado con sistema de roles.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Usuario(AbstractUser):
    """
    Modelo de Usuario personalizado extendiendo AbstractUser.
    Incluye sistema de roles: Propietario, Administrador, Empleado.
    """

    ROLE_CHOICES = [
        ('PROPIETARIO', settings.ROLES['PROPIETARIO']),
        ('ADMINISTRADOR', settings.ROLES['ADMINISTRADOR']),
        ('EMPLEADO', settings.ROLES['EMPLEADO']),
    ]

    # Campos adicionales
    rol = models.CharField(
        'Rol',
        max_length=20,
        choices=ROLE_CHOICES,
        default='EMPLEADO'
    )
    telefono = models.CharField('Teléfono', max_length=20, blank=True)
    direccion = models.CharField('Dirección', max_length=255, blank=True)
    foto = models.ImageField(
        'Foto de perfil',
        upload_to='usuarios/fotos/',
        null=True,
        blank=True
    )
    is_active = models.BooleanField('Activo', default=True)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_rol_display()})"

    @property
    def es_propietario(self):
        """Verifica si el usuario es propietario."""
        return self.rol == 'PROPIETARIO'

    @property
    def es_administrador(self):
        """Verifica si el usuario es administrador o propietario."""
        return self.rol in ['PROPIETARIO', 'ADMINISTRADOR']

    @property
    def es_empleado(self):
        """Verifica si el usuario es empleado."""
        return self.rol == 'EMPLEADO'

    def tiene_permiso(self, permiso):
        """
        Verifica si el usuario tiene un permiso específico según su rol.
        Args:
            permiso (str): El permiso a verificar
        Returns:
            bool: True si tiene el permiso
        """
        # Propietario tiene todos los permisos
        if self.es_propietario:
            return True

        # Mapeo de permisos por rol
        permisos_por_rol = {
            'ADMINISTRADOR': [
                'ver_dashboard',
                'gestionar_clientes',
                'gestionar_proveedores',
                'gestionar_productos',
                'ver_inventario',
                'gestionar_compras',
                'gestionar_ventas',
                'gestionar_cobranzas',
                'ver_reportes',
            ],
            'EMPLEADO': [
                'ver_dashboard',
                'ver_clientes',
                'crear_clientes',
                'ver_productos',
                'gestionar_ventas',
                'gestionar_cobranzas',
                'ver_reportes_basicos',
            ],
        }

        return permiso in permisos_por_rol.get(self.rol, [])
