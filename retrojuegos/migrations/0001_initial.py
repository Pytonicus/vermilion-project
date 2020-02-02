# Generated by Django 2.2.7 on 2019-11-24 13:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Sistema')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Retrojuego',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('original_title', models.CharField(max_length=200, verbose_name='Título Original')),
                ('serial_number', models.CharField(max_length=30, verbose_name='Número de Serie')),
                ('players', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, verbose_name='Jugadores')),
                ('date_released', models.DateField(verbose_name='Fecha de Publicación')),
                ('cover', models.ImageField(upload_to='retrogames/covers', verbose_name='Carátula')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción')),
                ('region', models.CharField(blank=True, choices=[('PAL', 'PAL - Europa'), ('NTCSU', 'NTCS-U - America'), ('NTCSJ', 'NTCS-J - Japón')], max_length=10, verbose_name='Región')),
                ('support', models.CharField(choices=[('CAR', 'Cartucho'), ('CD', 'CD-ROM'), ('DVD', 'DVD'), ('GD', 'GD-ROM'), ('UMD', 'UMD'), ('TA', 'Tarjeta')], max_length=10, verbose_name='Soporte')),
                ('number_disk', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, verbose_name='Discos')),
                ('screen_one', models.ImageField(upload_to='retrogames/screens', verbose_name='Captura 1')),
                ('screen_two', models.ImageField(upload_to='retrogames/screens', verbose_name='Captura 2')),
                ('screen_three', models.ImageField(upload_to='retrogames/screens', verbose_name='Captura 3')),
                ('screen_four', models.ImageField(upload_to='retrogames/screens', verbose_name='Captura 4')),
                ('as_downloaded', models.BooleanField(default=False, verbose_name='Subido')),
                ('download_link', models.URLField(blank=True, verbose_name='Link de Descarga')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('console', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retrojuegos.Console', verbose_name='Sistema')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opciones.Developer', verbose_name='Desarrollador')),
                ('extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opciones.Extension', verbose_name='Formato de Archivo')),
                ('genre', models.ManyToManyField(to='opciones.Genre', verbose_name='Género')),
                ('languages', models.ManyToManyField(to='opciones.Language', verbose_name='Idiomas')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opciones.Produced', verbose_name='Productora')),
            ],
            options={
                'verbose_name': 'Videojuego Retro',
                'verbose_name_plural': 'Videojuegos Retro',
                'ordering': ['title'],
            },
        ),
    ]
