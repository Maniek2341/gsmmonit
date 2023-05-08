# Generated by Django 4.0.5 on 2023-05-02 16:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0008_serwisraport_pracownicy_szt_serwisraport_pracownik'),
    ]

    operations = [
        migrations.AddField(
            model_name='serwisraport',
            name='hour_end',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='serwisraport',
            name='pracownicy_szt',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]