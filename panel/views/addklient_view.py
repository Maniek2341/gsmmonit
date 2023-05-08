import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import AddClientForm


class AddKlientView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        context = {
            'klient_form': AddClientForm(),
        }
        return render(request, 'panel/klienci/addklient.html', context)

    def post(self, request):
        klient_form = AddClientForm(request.POST)

        context = {
            'klient_form': klient_form
        }

        if klient_form.is_valid():
            form = klient_form.save()
            form.save()
            messages.success(request, json.dumps(
                {
                    'body': "Pomyślnie dodano klienta",
                    'title': "Dodano!"
                }
            ))

            return HttpResponseRedirect(reverse_lazy("dashboard"))

        else:
            messages.success(request, json.dumps(
                {
                    'body': "Nie udało się dodać klienta",
                    'title': "Błąd!"
                }
            ))

        return render(request, "panel/klienci/addklient.html", context)