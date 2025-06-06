# Generated by Django 5.2.1 on 2025-05-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrulleros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignacionrespuesta',
            options={'ordering': ['fecha_asignacion'], 'verbose_name': 'Asignación de Respuesta', 'verbose_name_plural': 'Asignaciones de Respuesta'},
        ),
        migrations.AlterModelOptions(
            name='patrullero',
            options={'ordering': ['placa'], 'verbose_name': 'Patrullero', 'verbose_name_plural': 'Patrulleros'},
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='creadodate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='creadopor',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='editadodate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='editadopor',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='eliminadodate',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='asignacionrespuesta',
            name='eliminadopor',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patrullero',
            name='creadodate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='patrullero',
            name='creadopor',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patrullero',
            name='editadodate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='patrullero',
            name='editadopor',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patrullero',
            name='eliminadodate',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='patrullero',
            name='eliminadopor',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patrullero',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
