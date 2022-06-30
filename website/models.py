from django.db import models

# Create your models here.

class Kontakt(models.Model):
    imie = models.CharField(max_length=50)
    email = models.EmailField()
    temat = models.CharField(max_length=150)
    phone = models.IntegerField()
    tresc = models.TextField(max_length=255)
