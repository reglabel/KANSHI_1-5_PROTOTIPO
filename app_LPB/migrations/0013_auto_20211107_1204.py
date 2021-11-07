# Generated by Django 3.2.9 on 2021-11-07 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_LPB', '0012_auto_20211106_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='duracao',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='hora_criacao',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='hora_notificacao',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='ano_criacao',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxLengthValidator(4)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='criacao_hora',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='criacao_minutos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='dia_criacao',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='duracao_horas',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='duracao_minutos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='duracao_segundos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='mes_criacao',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='notificacao_hora',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='notificacao_minutos',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59)]),
        ),
    ]
