# Generated by Django 3.0.2 on 2020-03-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascotas', '0002_mascotaperdida_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascotaperdida',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]