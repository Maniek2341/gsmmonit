import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import AddClientForm
from panel.models import Klient


class DeleteKlientView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        klient = Klient.objects.get(pk=pk)
        context = {
            'klient': klient
        }
        return render(request, 'panel/klienci/deleteklient.html', context)

    def post(self, request, pk):
        klient = Klient.objects.get(pk=pk)

        messages.info(request, json.dumps(
            {
                'body': "Pomyślnie usunięto klienta %s" % klient.nazwa_firmy,
                'title': "Usunięto!"
            }
        ))

        klient.delete()
        return HttpResponseRedirect(reverse_lazy("list_klient"))

