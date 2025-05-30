from django.db import models
from crum import get_current_user
# Create your models here.

class Zona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Zona')
    descripcion = models.TextField(blank=True, null=True)
    nivel_riesgo = models.IntegerField(default=0, verbose_name='Nivel de Riesgo')
    geom = models.TextField(blank=True, null=True, verbose_name='Geometría')
    ciudad = models.ForeignKey('sistema.Ciudad', on_delete=models.PROTECT, related_name='zonas')

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
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

class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    direccion = models.CharField(max_length=255)
    zona_riesgo = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    zona = models.ForeignKey('geolocalizacion.Zona', on_delete=models.CASCADE)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'
        ordering = ['direccion']

    def __str__(self):
        return self.direccion

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
