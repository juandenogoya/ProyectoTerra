"""
Modelos base abstractos para Terra Retail.
Estos modelos proveen funcionalidad común a todas las apps.
"""

from django.db import models
from django.contrib.auth import get_user_model


class TimeStampedModel(models.Model):
    """
    Modelo abstracto que provee campos de timestamp automáticos.
    """
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizado', auto_now=True)

    class Meta:
        abstract = True


class AuditedModel(TimeStampedModel):
    """
    Modelo abstracto con auditoría completa (timestamps + usuarios).
    """
    created_by = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created',
        verbose_name='Creado por'
    )
    updated_by = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_updated',
        verbose_name='Actualizado por'
    )

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """
    Modelo abstracto para soft delete (borrado lógico).
    """
    is_active = models.BooleanField('Activo', default=True)
    deleted_at = models.DateTimeField('Eliminado', null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        """Marca el registro como eliminado."""
        from django.utils import timezone
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        """Restaura un registro eliminado."""
        self.is_active = True
        self.deleted_at = None
        self.save()


class BaseModel(AuditedModel, SoftDeleteModel):
    """
    Modelo base que combina timestamp, auditoría y soft delete.
    Usar este para la mayoría de los modelos del sistema.
    """
    class Meta:
        abstract = True
