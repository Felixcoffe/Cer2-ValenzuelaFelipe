# Generated by Django 4.1.2 on 2022-11-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_correspondencia_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondencia',
            name='Destino',
            field=models.IntegerField(null=True),
        ),
    ]
