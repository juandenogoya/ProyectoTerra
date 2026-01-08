"""
Modelos de Productos para Terra Retail.
Sistema con variantes (tallas, colores) y categorías.
"""

from django.db import models
from django.core.validators import MinValueValidator
from apps.core.models import BaseModel, TimeStampedModel


class Categoria(TimeStampedModel):
    """
    Categoría de productos (Indumentaria, Calzado, etc.).
    """
    nombre = models.CharField('Nombre', max_length=100, unique=True)
    descripcion = models.TextField('Descripción', blank=True)
    padre = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subcategorias',
        verbose_name='Categoría Padre'
    )
    orden = models.IntegerField('Orden', default=0)
    is_active = models.BooleanField('Activa', default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['orden', 'nombre']

    def __str__(self):
        if self.padre:
            return f"{self.padre.nombre} > {self.nombre}"
        return self.nombre


class Talla(TimeStampedModel):
    """
    Tallas de productos (XS, S, M, L, XL o números de calzado).
    """
    nombre = models.CharField('Nombre', max_length=20, unique=True)
    orden = models.IntegerField('Orden', default=0)
    is_active = models.BooleanField('Activa', default=True)

    class Meta:
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'
        ordering = ['orden', 'nombre']

    def __str__(self):
        return self.nombre


class Color(TimeStampedModel):
    """
    Colores de productos.
    """
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    codigo_hex = models.CharField(
        'Código HEX',
        max_length=7,
        blank=True,
        help_text='Código de color hexadecimal (ejemplo: #FF0000)'
    )
    is_active = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(BaseModel):
    """
    Modelo base de Producto.
    """

    # Información básica
    codigo = models.CharField('Código', max_length=50, unique=True)
    nombre = models.CharField('Nombre', max_length=200)
    descripcion = models.TextField('Descripción', blank=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos',
        verbose_name='Categoría'
    )

    # Proveedor
    proveedor = models.ForeignKey(
        'proveedores.Proveedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='productos',
        verbose_name='Proveedor'
    )

    # Precios
    precio_costo = models.DecimalField(
        'Precio de Costo',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    precio_venta = models.DecimalField(
        'Precio de Venta',
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    precio_promocion = models.DecimalField(
        'Precio de Promoción',
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
    en_promocion = models.BooleanField('En Promoción', default=False)

    # Stock
    stock_minimo = models.IntegerField(
        'Stock Mínimo',
        default=0,
        validators=[MinValueValidator(0)]
    )

    # Código de barras
    codigo_barras = models.CharField(
        'Código de Barras',
        max_length=50,
        blank=True,
        unique=True,
        null=True
    )

    # Imagen
    imagen = models.ImageField(
        'Imagen',
        upload_to='productos/',
        null=True,
        blank=True
    )

    # Tiene variantes
    tiene_variantes = models.BooleanField('Tiene Variantes', default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['codigo']
        indexes = [
            models.Index(fields=['codigo']),
            models.Index(fields=['nombre']),
            models.Index(fields=['codigo_barras']),
        ]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    @property
    def precio_final(self):
        """Retorna el precio final considerando promoción."""
        if self.en_promocion and self.precio_promocion:
            return self.precio_promocion
        return self.precio_venta

    @property
    def margen_ganancia(self):
        """Calcula el margen de ganancia porcentual."""
        if self.precio_costo > 0:
            return ((self.precio_venta - self.precio_costo) / self.precio_costo) * 100
        return 0

    @property
    def stock_total(self):
        """Calcula el stock total de todas las variantes."""
        if self.tiene_variantes:
            return self.variantes.aggregate(
                total=models.Sum('stock')
            )['total'] or 0
        return 0

    @property
    def stock_bajo(self):
        """Verifica si el stock está por debajo del mínimo."""
        return self.stock_total < self.stock_minimo


class ProductoVariante(BaseModel):
    """
    Variante de producto (combinación de talla y color).
    """
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name='variantes',
        verbose_name='Producto'
    )
    talla = models.ForeignKey(
        Talla,
        on_delete=models.PROTECT,
        related_name='variantes',
        verbose_name='Talla'
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
        related_name='variantes',
        verbose_name='Color'
    )

    # Stock específico de esta variante
    stock = models.IntegerField(
        'Stock',
        default=0,
        validators=[MinValueValidator(0)]
    )

    # SKU único para la variante
    sku = models.CharField(
        'SKU',
        max_length=100,
        unique=True,
        help_text='Código único de la variante'
    )

    class Meta:
        verbose_name = 'Variante de Producto'
        verbose_name_plural = 'Variantes de Productos'
        unique_together = [['producto', 'talla', 'color']]
        ordering = ['producto', 'talla', 'color']

    def __str__(self):
        return f"{self.producto.nombre} - {self.talla} - {self.color}"

    def save(self, *args, **kwargs):
        """Genera SKU automáticamente si no existe."""
        if not self.sku:
            self.sku = f"{self.producto.codigo}-{self.talla.nombre}-{self.color.nombre}"
        super().save(*args, **kwargs)

    @property
    def stock_disponible(self):
        """Verifica si hay stock disponible."""
        return self.stock > 0
