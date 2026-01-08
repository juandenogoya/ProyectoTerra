"""
Formularios para la gestión de proveedores.
"""

from django import forms
from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    """
    Formulario para crear y editar proveedores.
    """

    class Meta:
        model = Proveedor
        fields = [
            'razon_social', 'nombre_fantasia', 'cuit', 'tipo_proveedor',
            'email', 'telefono', 'sitio_web',
            'calle', 'numero', 'piso', 'localidad', 'provincia', 'codigo_postal', 'pais',
            'condiciones_pago', 'descuento_pronto_pago', 'plazo_entrega_dias',
            'contacto_nombre', 'contacto_telefono', 'contacto_email',
            'notas'
        ]
        widgets = {
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            else:
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
