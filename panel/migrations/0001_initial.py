# Generated by Django 4.0.5 on 2023-04-19 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_firmy', models.CharField(max_length=80)),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('nip', models.IntegerField()),
                ('ulica', models.CharField(max_length=50)),
                ('kod_pocztowy', models.IntegerField()),
                ('miejscowosc', models.CharField(max_length=50)),
                ('telefon', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Klient',
                'verbose_name_plural': 'Klienci',
            },
        ),
        migrations.CreateModel(
            name='SerwisRaport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_start', models.DateTimeField()),
                ('data_end', models.DateTimeField()),
                ('wykonane_prace', models.TextField(max_length=250)),
                ('robocizna', models.IntegerField()),
                ('dojazd', models.IntegerField()),
                ('rodzaj_prac', models.PositiveSmallIntegerField(choices=[(1, 'Naprawa'), (2, 'Rozbudowa'), (3, 'Montaż'), (4, 'Przegląd'), (5, 'Zgranie')], default=1)),
                ('firma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firma', to='panel.klient')),
            ],
            options={
                'verbose_name': 'Raport serwisowy',
                'verbose_name_plural': 'Raporty serwisowe',
            },
        ),
    ]