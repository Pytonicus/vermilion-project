# Generated by Django 2.2.7 on 2019-11-26 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='staff',
            field=models.ManyToManyField(to='opciones.Staff', verbose_name='Reparto'),
        ),
    ]
