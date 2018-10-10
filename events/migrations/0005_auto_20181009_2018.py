# Generated by Django 2.0.8 on 2018-10-09 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180913_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-date', '-priority', 'event')},
        ),
        migrations.AlterField(
            model_name='event',
            name='event',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='event',
            name='priority',
            field=models.CharField(choices=[('0', 'Sem prioridade'), ('1', 'Normal'), ('2', 'Urgente'), ('3', 'Muito Urgente')], max_length=1),
        ),
    ]
