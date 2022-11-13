# Generated by Django 4.1.2 on 2022-11-13 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_llegada', models.DateField()),
                ('Estado', models.CharField(choices=[('En Consejeria', 'En Consejeria'), ('Entregada', 'Entregada')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Recidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_recidencia', models.IntegerField()),
                ('Propietario', models.CharField(max_length=30)),
                ('Estado', models.CharField(choices=[('Ocupado', 'Ocupado'), ('Disponible', 'Disponible'), ('En Mantenimiento', 'En mantenimiento')], max_length=30)),
            ],
        ),
    ]