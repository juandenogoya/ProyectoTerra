"""
Formularios para la gestión de productos.
"""

from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """
    Formulario para crear y editar productos.
    """

    class Meta:
        model = Producto
        fields = [
            'codigo', 'nombre', 'descripcion', 'categoria', 'proveedor',
            'precio_costo', 'precio_venta', 'precio_promocion', 'en_promocion',
            'stock_minimo', 'codigo_barras', 'imagen', 'tiene_variantes'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'rounded text-blue-600 focus:ring-2 focus:ring-blue-500'
            elif not isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
