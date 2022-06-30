from django import forms

from website.models import Kontakt


class ContactForm(forms.ModelForm):
    imie = forms.CharField(
        label='Imię',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    temat = forms.CharField(
        label='Temat',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    phone = forms.IntegerField(
        label='Nr. telefonu',
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    tresc = forms.CharField(
        label='Treść wiadomości',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Kontakt
        fields = '__all__'
