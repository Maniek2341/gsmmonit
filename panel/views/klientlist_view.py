from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.models import Klient


class KlientListView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        queryset = Klient.objects.all()
        context = {
            'klients': queryset,
        }
        return render(request, 'panel/klienci/klient_list.html', context)
