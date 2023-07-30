from django.contrib.auth.models import User
from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


# Create your models here.

class Klient(models.Model):
    nazwa_firmy = models.CharField(max_length=150)
    imie = models.CharField(max_length=50, null=True, blank=True)
    nazwisko = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nip = models.BigIntegerField(null=True, blank=True)
    ulica = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=50)
    kraj = models.CharField(max_length=50, null=True, blank=True)
    miejscowosc = models.CharField(max_length=50)
    telefon = models.IntegerField(null=True, blank=True)
    czy_firma = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Klient'
        verbose_name_plural = 'Klienci'

    def __str__(self):
        return self.nazwa_firmy

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "Klient_{0}/{1}/{2}".format(instance.firma, instance.data_end, filename)

class SerwisRaport(models.Model):
    RODZAJ_NAPRAWA = 1
    RODZAJ_ROZBUDOWA = 2
    RODZAJ_MONTAZ = 3
    RODZAJ_PRZEGLAD = 4
    RODZAJ_ZGRANIE = 5
    RODZAJ_CHOICES = [
        (RODZAJ_NAPRAWA, "Naprawa"),
        (RODZAJ_ROZBUDOWA, "Rozbudowa"),
        (RODZAJ_MONTAZ, "Montaż"),
        (RODZAJ_PRZEGLAD, "Przegląd"),
        (RODZAJ_ZGRANIE, "Zgranie"),
    ]

    STATUS_NOWE = 1
    STATUS_ZAFAKTUROWANE = 2
    STATUS_WYSLANE = 3
    STATUS_GWARANCJA = 4

    STATUS_CHOICES = [
        (STATUS_NOWE, "Nowe"),
        (STATUS_ZAFAKTUROWANE, "Zafakturowane"),
        (STATUS_WYSLANE, "Wysłane"),
        (STATUS_GWARANCJA, "Gwarancja"),
    ]

    firma = models.ForeignKey(Klient, related_name="firma", on_delete=models.CASCADE, blank=True, null=True)
    data_end = models.DateField(blank=True, null=True)
    hour_end = models.TimeField(default=timezone.now)
    wykonane_prace = models.TextField(max_length=250, blank=True, null=True)
    urzadzenia = models.TextField(max_length=250, blank=True, null=True)
    robocizna = models.FloatField(blank=True, null=True)
    dojazd = models.IntegerField(blank=True, null=True)
    rodzaj_prac = models.PositiveSmallIntegerField(choices=RODZAJ_CHOICES, default=RODZAJ_NAPRAWA)
    pracownik = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, blank=True, null=True)
    pracownicy_szt = models.IntegerField(blank=True, null=True, default=1)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_NOWE, blank=True, null=True)
    zdjecie = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie2 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie3 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie4 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie5 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie6 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie7 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    zdjecie8 = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    class Meta:
        verbose_name = 'Raport serwisowy'
        verbose_name_plural = 'Raporty serwisowe'

    def __str__(self):
        return f"Serwis w: {self.firma.nazwa_firmy} o {self.data_end}"
