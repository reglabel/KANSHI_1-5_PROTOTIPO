# Generated by Django 3.2.9 on 2021-11-07 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_LPB', '0014_auto_20211107_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_e_hora_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
