# Generated by Django 3.2.3 on 2021-06-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_arriendos_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendos',
            name='fecha_inicio',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='arriendos',
            name='fecha_termino',
            field=models.DateTimeField(null=True),
        ),
    ]
