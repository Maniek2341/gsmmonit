import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
import googlemaps

from GSM import settings
from panel.models import SerwisRaport


class RaportDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)

        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)

        calculate = json.dumps(gmaps.distance_matrix("Przysiecz Stawowa 2",
                                                     raport.firma.miejscowosc + raport.firma.ulica,
                                                     mode="driving"))

        calculate2 = json.loads(calculate)

        distance = calculate2['rows'][0]['elements'][0]['distance']['text']
        km = distance[:-2]
        obakierunki = (float(km) * 2)

        cenadojazd = round(float(obakierunki) * 1.15,2)
        cenarobocizna = raport.robocizna * 80
        cenarobocizna2 = raport.robocizna * 120
        razem1 = cenadojazd + cenarobocizna
        razem2 = cenadojazd + cenarobocizna2



        context = {
            'raport': raport,
            'dojazd': cenadojazd,
            'robocizna': cenarobocizna,
            'robocizna2': cenarobocizna2,
            'razem1': razem1,
            'razem2': razem2,
            'dystans': km,
            'mapydojazd': obakierunki
        }
        return render(request, 'panel/raportyserwisowe/raportdetail.html', context)

    def post(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)

        messages.success(request, json.dumps(
            {
                'body': "Pomyślnie zmieniono status na wysłane",
                'title': "Zmieniono!"
            }
        ))

        raport.status = 3
        raport.save()
        return HttpResponseRedirect(reverse_lazy("list_raport"))
