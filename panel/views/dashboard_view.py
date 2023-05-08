from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.models import Klient, SerwisRaport


class DashboardView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        ostatnieraporty = SerwisRaport.objects.all().order_by("-data_end")[:10]
        klienci = Klient.objects.all().count()
        raporty = SerwisRaport.objects.all().count()
        context = {
            'all_klients': klienci,
            'all_raports': raporty,
            'ostatnieraporty': ostatnieraporty,
        }
        return render(request, 'panel/main.html', context)
