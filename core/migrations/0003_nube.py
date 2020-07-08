# Generated by Django 3.0.1 on 2020-02-03 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191124_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('categoria', models.CharField(max_length=150, verbose_name='Categoría')),
                ('nube', models.CharField(max_length=150, verbose_name='Nube')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Subida')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='Resubido el')),
            ],
            options={
                'verbose_name': 'Nube de datos',
                'verbose_name_plural': 'Datos en la nube',
                'ordering': ['-nube'],
            },
        ),
    ]