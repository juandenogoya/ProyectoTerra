"""
Modelo de Proveedor para Terra Retail.
"""

from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from apps.core.models import BaseModel


class Proveedor(BaseModel):
    """
    Modelo de Proveedor.
    """

    TIPO_PROVEEDOR_CHOICES = [
        ('NACIONAL', 'Nacional'),
        ('INTERNACIONAL', 'Internacional'),
    ]

    # Información de la empresa
    razon_social = models.CharField('Razón Social', max_length=200)
    nombre_fantasia = models.CharField('Nombre de Fantasía', max_length=200, blank=True)
    cuit = models.CharField('CUIT', max_length=13, unique=True)
    tipo_proveedor = models.CharField(
        'Tipo de Proveedor',
        max_length=20,
        choices=TIPO_PROVEEDOR_CHOICES,
        default='NACIONAL'
    )

    # Contacto principal
    email = models.EmailField(
        'Email',
        validators=[EmailValidator()]
    )
    telefono = models.CharField(
        'Teléfono',
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Ingrese un número de teléfono válido'
            )
        ]
    )
    sitio_web = models.URLField('Sitio Web', blank=True)

    # Dirección
    calle = models.CharField('Calle', max_length=100)
    numero = models.CharField('Número', max_length=10)
    piso = models.CharField('Piso', max_length=10, blank=True)
    localidad = models.CharField('Localidad', max_length=100)
    provincia = models.CharField('Provincia', max_length=100)
    codigo_postal = models.CharField('Código Postal', max_length=10)
    pais = models.CharField('País', max_length=100, default='Argentina')

    # Información comercial
    condiciones_pago = models.CharField(
        'Condiciones de Pago',
        max_length=200,
        help_text='Ejemplo: 30/60/90 días'
    )
    descuento_pronto_pago = models.DecimalField(
        'Descuento Pronto Pago (%)',
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    plazo_entrega_dias = models.IntegerField(
        'Plazo de Entrega (días)',
        default=0
    )

    # Contactos adicionales
    contacto_nombre = models.CharField('Contacto - Nombre', max_length=100, blank=True)
    contacto_telefono = models.CharField('Contacto - Teléfono', max_length=20, blank=True)
    contacto_email = models.EmailField('Contacto - Email', blank=True)

    # Observaciones
    notas = models.TextField('Notas', blank=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['razon_social']
        indexes = [
            models.Index(fields=['cuit']),
            models.Index(fields=['razon_social']),
        ]

    def __str__(self):
        if self.nombre_fantasia:
            return f"{self.nombre_fantasia} ({self.cuit})"
        return f"{self.razon_social} ({self.cuit})"

    @property
    def nombre_display(self):
        """Retorna el nombre para mostrar."""
        return self.nombre_fantasia or self.razon_social

    @property
    def direccion_completa(self):
        """Retorna la dirección completa formateada."""
        direccion = f"{self.calle} {self.numero}"
        if self.piso:
            direccion += f", Piso {self.piso}"
        direccion += f", {self.localidad}, {self.provincia} ({self.codigo_postal})"
        return direccion
