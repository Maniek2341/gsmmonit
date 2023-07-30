import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.models import SerwisRaport


class RaportFakturaView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)
        context = {
            'raport': raport,
        }
        return render(request, 'panel/raportyserwisowe/raportdetail.html', context)

    def post(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)


        messages.success(request, json.dumps(
            {
                'body': "Pomyślnie zmieniono status na zafakturowane",
                'title': "Zmieniono!"
            }
        ))
        raport.status = 2
        raport.save()

        return HttpResponseRedirect(reverse_lazy("list_raport"))
