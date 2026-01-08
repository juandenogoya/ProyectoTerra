"""
URL configuration for Terra Retail project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Apps
    path('', include('apps.core.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('proveedores/', include('apps.proveedores.urls')),
    path('productos/', include('apps.productos.urls')),

    # Redirect root to dashboard
    path('', RedirectView.as_view(pattern_name='core:dashboard'), name='home'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    # Debug toolbar
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

# Customizar admin
admin.site.site_header = 'Terra Retail Admin'
admin.site.site_title = 'Terra Retail'
admin.site.index_title = 'Panel de Administración'
