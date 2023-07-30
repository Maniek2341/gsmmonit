from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.models import SerwisRaport


class FakturyWyslaneView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        queryset = SerwisRaport.objects.filter(status=3)
        context = {
            'raports': queryset,
        }
        return render(request, 'panel/faktury/fakturywyslane.html', context)
