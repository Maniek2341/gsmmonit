from django.shortcuts import render
from django.views import View


class SieciView(View):
    def get(self, request):
        context = {
            'title': 'Instalacje sieciowe',
            'description': 'Tworzymy instalacje sieciowe dla szkół, firm jak i osób prywatnych.',
            'keywords': 'sieci, instalacje sieciowe, opole',
        }
        return render(request, 'sites/web/sieci.html', context)
