from django.db import models
from crum import get_current_user
# Create your models here.

class Reporte(models.Model):
    TIPO = (
        ('INCENDIO', 'Incendio'),
        ('INUNDACION', 'Inundación'),
        ('SISMO', 'Sismo'),
        ('OTRO', 'Otro'),
    )
    ESTADO = (
        ('NUEVO', 'Nuevo'),
        ('EN_PROCESO', 'En Proceso'),
        ('CERRADO', 'Cerrado'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO)
    descripcion = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    anonimo = models.BooleanField(default=False)
    prioridad = models.PositiveSmallIntegerField(default=3)
    ubicacion = models.ForeignKey('geolocalizacion.Ubicacion', on_delete=models.CASCADE)
    alerta = models.ForeignKey('alertas.Alerta', null=True, blank=True, on_delete=models.SET_NULL)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.tipo} - {self.fecha_hora}"

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

class Evidencia(models.Model):
    TIPO = (
        ('IMAGEN', 'Imagen'),
        ('VIDEO', 'Video'),
        ('DOCUMENTO', 'Documento'),
        ('OTRO', 'Otro'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO)
    url = models.URLField()
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    reporte = models.ForeignKey('reportes.Reporte', on_delete=models.CASCADE)
    tipo_archivo = models.CharField(max_length=20)
    hash = models.CharField(max_length=128)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Evidencia'
        verbose_name_plural = 'Evidencias'
        ordering = ['-fecha_subida']

    def __str__(self):
        return f"{self.tipo} - {self.url}"

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

class IARegistro(models.Model):
    modelo = models.CharField(max_length=100)
    evento_detectado = models.CharField(max_length=100)
    confianza = models.FloatField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    evidencia = models.ForeignKey(Evidencia, on_delete=models.CASCADE)
    reporte = models.ForeignKey('reportes.Reporte', null=True, blank=True, on_delete=models.SET_NULL)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'IARegistro'
        verbose_name_plural = 'IARegistros'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.modelo} - {self.evento_detectado}"


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
