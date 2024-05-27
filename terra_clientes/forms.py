from django import forms
from .models import *

class AltaClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Especificar el modelo asociado
        fields = ['nombre', 'apellido', 'num_doc', 'email', 'telefono',
                  'num_dir', 'calle', 'localidad', 'provincia', 'pais']

