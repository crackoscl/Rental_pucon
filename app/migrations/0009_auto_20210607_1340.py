# Generated by Django 3.2.3 on 2021-06-07 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210606_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendos',
            name='fecha_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='arriendos',
            name='fecha_termino',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
