from django.db import models
from crum import get_current_user

# Create your models here.

class DispositivoIoT(models.Model):
    TIPO = (
        ('SIRENA', 'Sirena'),
        ('SENSOR', 'Sensor'),
        ('CAMARA', 'Cámara'),
    )
    ESTADO = (
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('MANTENIMIENTO', 'Mantenimiento'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO)
    estado = models.CharField(max_length=20, choices=ESTADO)
    codigo_serie = models.CharField(max_length=100)
    ubicacion = models.ForeignKey('geolocalizacion.Ubicacion', on_delete=models.PROTECT)
    fecha_instalacion = models.DateTimeField(null=True, blank=True)
    estado_conexion = models.CharField(max_length=10, choices=[('online', 'Online'), ('offline', 'Offline')], default='online')
    ultimo_ping = models.DateTimeField(null=True, blank=True)
    centro_monitoreo = models.ForeignKey('centro_monitoreo.CentroMonitoreo', null=True, blank=True, on_delete=models.SET_NULL)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = 'Dispositivo IoT'
        verbose_name_plural = 'Dispositivos IoT'
        ordering = ['-fecha_instalacion']

    def __str__(self):
        return f"{self.tipo} - {self.codigo_serie}"


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

class LogDispositivo(models.Model):
    dispositivo = models.ForeignKey(DispositivoIoT, on_delete=models.CASCADE)
    evento = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True,null=True)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadodate = models.DateTimeField(auto_now=True,null=True)
    eliminadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    eliminadodate = models.DateTimeField(blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return f"{self.dispositivo} - {self.evento}"

    class Meta:
        verbose_name = 'LogDispositivo IoT' # singular
        verbose_name_plural = 'LogDispositivos IoT' # plural
        ordering = ['-fecha_hora']


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
