"""
Modelo de Cliente para Terra Retail.
"""

from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from apps.core.models import BaseModel


class Cliente(BaseModel):
    """
    Modelo de Cliente con información completa.
    """

    TIPO_CLIENTE_CHOICES = [
        ('MINORISTA', 'Minorista'),
        ('MAYORISTA', 'Mayorista'),
        ('VIP', 'VIP'),
    ]

    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'DNI'),
        ('CUIT', 'CUIT'),
        ('CUIL', 'CUIL'),
        ('PASAPORTE', 'Pasaporte'),
    ]

    # Información personal
    tipo_documento = models.CharField(
        'Tipo de Documento',
        max_length=20,
        choices=TIPO_DOCUMENTO_CHOICES,
        default='DNI'
    )
    numero_documento = models.CharField(
        'Número de Documento',
        max_length=20,
        unique=True
    )
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100)
    email = models.EmailField(
        'Email',
        unique=True,
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
    fecha_nacimiento = models.DateField(
        'Fecha de Nacimiento',
        null=True,
        blank=True
    )

    # Dirección
    calle = models.CharField('Calle', max_length=100)
    numero = models.CharField('Número', max_length=10)
    piso = models.CharField('Piso', max_length=10, blank=True)
    departamento = models.CharField('Departamento', max_length=10, blank=True)
    localidad = models.CharField('Localidad', max_length=100)
    provincia = models.CharField('Provincia', max_length=100)
    codigo_postal = models.CharField('Código Postal', max_length=10)
    pais = models.CharField('País', max_length=100, default='Argentina')

    # Información comercial
    tipo_cliente = models.CharField(
        'Tipo de Cliente',
        max_length=20,
        choices=TIPO_CLIENTE_CHOICES,
        default='MINORISTA'
    )
    limite_credito = models.DecimalField(
        'Límite de Crédito',
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    saldo_actual = models.DecimalField(
        'Saldo Actual',
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    descuento_porcentaje = models.DecimalField(
        'Descuento (%)',
        max_digits=5,
        decimal_places=2,
        default=0.00
    )

    # Notas y observaciones
    notas = models.TextField('Notas', blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['numero_documento']),
            models.Index(fields=['email']),
            models.Index(fields=['apellido', 'nombre']),
        ]

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.numero_documento})"

    @property
    def nombre_completo(self):
        """Retorna el nombre completo del cliente."""
        return f"{self.nombre} {self.apellido}"

    @property
    def direccion_completa(self):
        """Retorna la dirección completa formateada."""
        direccion = f"{self.calle} {self.numero}"
        if self.piso:
            direccion += f", Piso {self.piso}"
        if self.departamento:
            direccion += f" Depto. {self.departamento}"
        direccion += f", {self.localidad}, {self.provincia} ({self.codigo_postal})"
        return direccion

    @property
    def credito_disponible(self):
        """Calcula el crédito disponible."""
        return self.limite_credito - self.saldo_actual

    @property
    def tiene_deuda(self):
        """Verifica si el cliente tiene deuda."""
        return self.saldo_actual > 0

    @property
    def puede_comprar_credito(self):
        """Verifica si el cliente puede comprar a crédito."""
        return self.credito_disponible > 0
