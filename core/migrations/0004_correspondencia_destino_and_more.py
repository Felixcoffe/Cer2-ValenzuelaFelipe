# Generated by Django 4.1.2 on 2022-11-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_residencia_num_residencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='Destino',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='residencia',
            name='Num_residencia',
            field=models.IntegerField(),
        ),
    ]
