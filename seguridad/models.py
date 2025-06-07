import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from crum import get_current_user
from django.contrib.auth.models import Group

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Usuario"), max_length=191, unique=True)
    first_name = models.CharField(verbose_name=_("Nombres"), max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name=_("Apellidos"), max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    foto = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        verbose_name='Archive Photo',
        max_length=1024,
        blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return '{}'.format(self.username)

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username

    def get_foto_url(self):
        return self.foto.url

class Modulo(models.Model):
    CLASE_RECURSO = (
        ('LISTA', 'LISTA'),
        ('ITEM', 'ITEM'),
    )
    TIPO_RECURSO = (
        ('Mantenimientos', 'MANTENIMIENTOS'),
        ('Documentos', 'DOCUMENTOS'),
        ('Procesos', 'PROCESOS'),
        ('Informes', 'INFORMES'),
        ('Seguridad', 'SEGURIDAD'),
    )
    padre = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    codigo = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    orden = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    ruta = models.CharField(max_length=1024, blank=True, null=True, editable=False)
    clase = models.CharField(max_length=10, blank=True, null=True, choices=CLASE_RECURSO)
    tipo = models.CharField(max_length=15, blank=True, null=True, choices=TIPO_RECURSO)
    icono = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    item_orden = models.IntegerField(default=0, blank=True, null=True)
    habilitado = models.BooleanField(default=False)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True)
    editadodate = models.DateTimeField(auto_now=True)
    pcid = models.CharField(max_length=200, blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} (/{self.url})'

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['item_orden']

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.codigo:
            self.codigo = self.codigo.upper()
        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)

        cid = str(self.id).zfill(6)

        if not self.padre is None:
            self.ruta = self.padre.ruta + '/' + cid
            self.orden = self.padre.orden + '/' + str(self.nombre)
        else:
            self.ruta = 'ROOT/' + cid
            self.orden = 'General/' + str(self.nombre)

        models.Model.save(self)

class ModuloGrupo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    modulos = models.ManyToManyField(Modulo)
    grupos = models.ManyToManyField(Group)
    prioridad = models.IntegerField(blank=True, null=True)
    creadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    editadopor = models.CharField(max_length=100, blank=True, null=True, editable=False)
    creadodate = models.DateTimeField(auto_now_add=True)
    editadodate = models.DateTimeField(auto_now=True)
    pcid = models.CharField(max_length=200, blank=True, null=True, editable=False)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.prioridad}'

    class Meta:
        verbose_name = 'Grupo de Módulos'
        verbose_name_plural = 'Grupos de Módulos'
        ordering = ['prioridad', 'nombre']

    def modulos_activos(self):
        return self.modulos.filter(activo=True).order_by('item_orden')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        try:
            user = get_current_user()

            if self._state.adding:
                self.creadopor = user.username
            else:
                self.editadopor = user.username
        except:
            pass

        models.Model.save(self)
