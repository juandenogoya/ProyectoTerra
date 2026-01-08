"""
Formularios para la gestión de clientes.
"""

from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    """
    Formulario para crear y editar clientes.
    """

    class Meta:
        model = Cliente
        fields = [
            'tipo_documento', 'numero_documento', 'nombre', 'apellido',
            'email', 'telefono', 'fecha_nacimiento',
            'calle', 'numero', 'piso', 'departamento',
            'localidad', 'provincia', 'codigo_postal', 'pais',
            'tipo_cliente', 'limite_credito', 'descuento_porcentaje',
            'notas'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agregar clases Tailwind a todos los campos
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            else:
                field.widget.attrs['class'] = 'w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
