# Generated by Django 4.0.5 on 2023-05-06 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0016_remove_serwisraport_pracownik'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serwisraport',
            name='status',
        ),
    ]
