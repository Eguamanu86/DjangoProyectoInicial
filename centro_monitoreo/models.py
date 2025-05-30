from django.db import models
from crum import get_current_user
# Create your models here.

class CentroMonitoreo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    coordinador = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    operadores = models.ManyToManyField('seguridad.User', related_name='centros_operados', blank=True)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Centro de Monitoreo'
        verbose_name_plural = 'Centros de Monitoreo'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        try:
            user = get_current_user()

            if self._state.adding:  # si estamos creando registro
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
