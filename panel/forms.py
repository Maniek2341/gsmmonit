from django import forms
from django.core.validators import FileExtensionValidator

from panel.models import Klient, SerwisRaport


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nazwa Użytkownika",
                "class": "form-control",
                "autocomplete": "username"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Hasło",
                "class": "form-control",
                "autocomplete": "current-password"
            }
        ))


class AddClientForm(forms.ModelForm):
    nazwa_firmy = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz nazwe firmy",
                "class": "form-control",
            }
        )
    )
    imie = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz imie",
                "class": "form-control",
            })
    )
    nazwisko = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz nazwisko",
                "class": "form-control",
            })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Wpisz e-mail",
                "class": "form-control",
            })
    )
    nip = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Wpisz nip",
                "class": "form-control",
            })
    )
    ulica = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz ulice i nr domu",
                "class": "form-control",
            })
    )
    kod_pocztowy = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz kod pocztowy",
                "class": "form-control",
            })
    )
    miejscowosc = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz miejscowość",
                "class": "form-control",
            })
    )
    telefon = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Wpisz nr telefonu",
                "class": "form-control",
            })
    )
    kraj = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Wpisz kraj",
                "class": "form-control",
            })
    )
    czy_firma = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
            })
    )

    class Meta:
        model = Klient
        fields = ['nazwa_firmy', 'imie', 'nazwisko', 'email', 'nip', 'ulica', 'kod_pocztowy', 'miejscowosc', 'telefon',
                  'czy_firma', 'kraj']


class AddRaportForm(forms.ModelForm):
    firma = forms.ModelChoiceField(
        queryset=Klient.objects.all(),
        initial=Klient.objects.filter(pk=1),
        widget=forms.Select(
            attrs={
                "class": "form-control select2"
            }
        )
    )

    data_end = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                'type': 'date'
            })
    )

    wykonane_prace = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 8,
                'style':'resize:none;',
                "placeholder": "Podaj wykonane prace od myślników",
                "class": "form-control",
            })
    )

    urzadzenia = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 8,
                'style': 'resize:none;',
                "placeholder": "Podaj wykorzystane urzadzenia wypisując od myślników a na końcu podając ilość",
                "class": "form-control",
            })
    )

    robocizna = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Wpisz ilość godzin spedzonych na serwisie",
                "class": "form-control",
            })
    )

    dojazd = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Podaj ilość km tam i spowrotem",
                "class": "form-control",
            })
    )

    pracownicy_szt = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Podaj ilość pracowników",
                "class": "form-control",
            })
    )

    rodzaj_prac = forms.ChoiceField(
        choices=SerwisRaport.RODZAJ_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            })
    )

    zdjecia = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "placeholder": "Wybierz",
                "class": "custom-file-input",
                "multiple": True,
            })
    )

    class Meta:
        model = SerwisRaport
        fields = ['firma', 'data_end', 'wykonane_prace', 'robocizna', 'dojazd', 'rodzaj_prac', 'zdjecia', 'urzadzenia', 'pracownicy_szt']
        exclude = ['pracownik']
