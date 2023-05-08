import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import AddClientForm
from panel.models import Klient


class EditKlientView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        klient = Klient.objects.get(pk=pk)
        klient_form = AddClientForm(instance=klient)
        context = {
            'klient': klient,
            'klient_form': klient_form
        }
        return render(request, 'panel/klienci/editklient.html', context)

    def post(self, request, pk):
        klient = Klient.objects.get(pk=pk)

        klient_form = AddClientForm(request.POST, instance=klient)

        context = {
            'klient_form': klient_form,
            'klient': klient,
        }

        if klient_form.is_valid():

            messages.info(request, json.dumps(
                {
                    'body': "Pomyślnie zaaktualizowaleś klienta",
                    'title': "Zaktualizowano poprawnie!"
                }
            ))
            klient_form.save()
            return HttpResponseRedirect(reverse_lazy("list_klient"))
        else:
            return render(request, 'panel/klienci/editklient.html', context)
