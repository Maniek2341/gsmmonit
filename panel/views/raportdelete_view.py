import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import AddClientForm
from panel.models import Klient, SerwisRaport


class DeleteRaportView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)
        context = {
            'raport': raport
        }
        return render(request, 'panel/raportyserwisowe/deleteraport.html', context)

    def post(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)

        messages.info(request, json.dumps(
            {
                'body': "Pomyślnie usunięto raport od klienta %s" % raport.firma.nazwa_firmy,
                'title': "Usunięto!"
            }
        ))

        raport.delete()
        return HttpResponseRedirect(reverse_lazy("list_raport"))

