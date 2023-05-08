import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import AddRaportForm
from panel.models import SerwisRaport


class EditRaportView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)
        raport_form = AddRaportForm(instance=raport)
        context = {
            'raport': raport,
            'raport_form': raport_form
        }
        return render(request, 'panel/raportyserwisowe/editraport.html', context)

    def post(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)

        raport_form = AddRaportForm(request.POST, instance=raport)

        context = {
            'raport_form': raport_form,
            'raport': raport,
        }

        if raport_form.is_valid():

            messages.info(request, json.dumps(
                {
                    'body': "Pomyślnie zaaktualizowaleś raport",
                    'title': "Zaktualizowano poprawnie!"
                }
            ))
            raport_form.save()
            return HttpResponseRedirect(reverse_lazy("list_raport"))
        else:
            return render(request, 'panel/raportyserwisowe/editraport.html', context)
