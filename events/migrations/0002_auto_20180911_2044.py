# Generated by Django 2.0.8 on 2018-09-11 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='events',
            new_name='event',
        ),
    ]
