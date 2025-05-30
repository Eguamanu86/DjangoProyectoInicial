from django.db import models
from crum import get_current_user

class Alerta(models.Model):
    TIPO_ALERTA = (
        ('INCENDIO', 'Incendio'),
        ('INUNDACION', 'Inundación'),
        ('SISMO', 'Sismo'),
        ('OTRO', 'Otro'),
    )
    GENERADO_POR = (
        ('USUARIO', 'Usuario'),
        ('SISTEMA', 'Sistema'),
        ('SENSOR', 'Sensor'),
    )

    tipo_alerta = models.CharField(max_length=20, choices=TIPO_ALERTA, verbose_name='Tipo de Alerta')
    nivel_urgencia = models.PositiveSmallIntegerField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    resuelta = models.BooleanField(default=False)
    ubicacion = models.ForeignKey('geolocalizacion.Ubicacion', on_delete=models.CASCADE)
    generado_por = models.CharField(max_length=30)
    dispositivo = models.ForeignKey('dispositivos.DispositivoIoT', null=True, blank=True, on_delete=models.SET_NULL)
    centro_monitoreo = models.ForeignKey('centro_monitoreo.CentroMonitoreo', on_delete=models.CASCADE)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.get_tipo_alerta_display()} - Urgencia {self.nivel_urgencia}"


    def save(self, force_insert=False, force_update=False, using=None, **kwargs):

        try:
            user = get_current_user()

            if self._state.adding: ## si estamos creando registro
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
