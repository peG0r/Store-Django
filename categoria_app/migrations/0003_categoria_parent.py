# Generated by Django 5.0.6 on 2024-06-01 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria_app', '0002_categoria_descripcion_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='categoria_app.categoria'),
        ),
    ]
