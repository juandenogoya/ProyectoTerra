"""
Context processors personalizados para Terra Retail.
"""

from django.conf import settings


def system_info(request):
    """
    Agrega información del sistema disponible en todos los templates.
    """
    return {
        'APP_NAME': 'Terra Retail',
        'APP_VERSION': '1.0.0',
        'ROLES': settings.ROLES,
    }
