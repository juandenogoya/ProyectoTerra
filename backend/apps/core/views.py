"""
Vistas principales de la aplicación.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    """
    Dashboard principal del sistema.
    """
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'pages/dashboard.html', context)
