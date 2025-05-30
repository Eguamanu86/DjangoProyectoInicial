from django.db import models
from crum import get_current_user

# Create your models here.

class EventoSistema(models.Model):
    ORIGEN = (
        ('USUARIO', 'Usuario'),
        ('SISTEMA', 'Sistema'),
        ('EXTERNO', 'Externo'),
    )
    TIPO = (
        ('INFO', 'Información'),
        ('ALERTA', 'Alerta'),
        ('ERROR', 'Error'),
    )

    descripcion = models.TextField()
    origen = models.CharField(max_length=20, choices=ORIGEN)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO)
    usuario = models.ForeignKey('seguridad.User', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Evento de Sistema'
        verbose_name_plural = 'Eventos de Sistema'
        ordering = ['-fecha_hora']


    def __str__(self):
        return f"{self.tipo} - {self.origen}"


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
