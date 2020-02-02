# Generated by Django 2.2.7 on 2019-12-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20191126_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='original_title',
            field=models.CharField(blank=True, max_length=150, verbose_name='Título original'),
        ),
        migrations.AlterField(
            model_name='serie',
            name='duration',
            field=models.TimeField(verbose_name='Duración por episodio'),
        ),
    ]
