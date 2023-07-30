import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import AddRaportForm
from panel.models import SerwisRaport


class AddRaportView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        context = {
            'raport_form': AddRaportForm(),
        }
        return render(request, 'panel/raportyserwisowe/addraport.html', context)

    def post(self, request):
        raport_form = AddRaportForm(request.POST, request.FILES)
        raport_form.instance.pracownik = request.user

        context = {
            'raport_form': raport_form
        }

        if raport_form.is_valid():
            form = raport_form.save()
            form.save()

            messages.success(request, json.dumps(
                {
                    'body': "Pomyślnie dodano raport",
                    'title': "Dodano!"
                }
            ))
            return HttpResponseRedirect(reverse_lazy("dashboard"))

        else:
            messages.success(request, json.dumps(
                {
                    'body': "Nie udało się dodać raportu",
                    'title': "Błąd!"
                }
            ))

        return render(request, "panel/raportyserwisowe/addraport.html", context)
