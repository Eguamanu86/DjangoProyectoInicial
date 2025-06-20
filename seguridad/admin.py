from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *

class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    model = User
    list_display = [
        "pkid",
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "email"]
    list_filter = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Photo Information"),
            {
                "fields": (
                    "foto",
                )
            },
        ),(
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name"
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ["email", "username", "first_name", "last_name"]
admin.site.register(User, UserAdmin)

class ModuloAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'nombre',
        'tipo',
        'clase',
        'item_orden',
        'activo',
    )
    list_per_page = 20
    ordering = ('tipo','nombre')
    search_fields = ('codigo','nombre')
    list_filter = (
        'tipo',
        'activo'
    )
admin.site.register(Modulo,ModuloAdmin)

class ModuloGrupoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'descripcion',
        'prioridad',
        'activo',
    )
    list_per_page = 20
    ordering = ('prioridad','nombre',)
    search_fields = ('nombre',)
    list_filter = (
        'activo',
    )
admin.site.register(ModuloGrupo,ModuloGrupoAdmin)
