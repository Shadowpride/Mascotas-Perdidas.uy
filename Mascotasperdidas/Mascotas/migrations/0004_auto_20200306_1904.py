# Generated by Django 3.0.3 on 2020-03-06 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mascotas', '0003_mascotaperdida_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotaperdida',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Mascotas.Estado'),
        ),
    ]
