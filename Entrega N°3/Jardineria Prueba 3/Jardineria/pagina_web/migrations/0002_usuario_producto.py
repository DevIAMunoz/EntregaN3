# Generated by Django 5.0.6 on 2024-06-30 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('rut', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=20)),
                ('confirmar_contraseña', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['id_usuario'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foto', models.ImageField(upload_to='productos')),
                ('activo', models.BooleanField(default=True)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina_web.categoria')),
            ],
            options={
                'ordering': ['id_producto'],
            },
        ),
    ]
