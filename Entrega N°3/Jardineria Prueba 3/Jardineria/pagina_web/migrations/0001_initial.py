# Generated by Django 5.0.6 on 2024-06-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
    ]
