from django.shortcuts import render
from django.views import View


class RealizacjeView(View):
    def get(self, request):
        context = {
            'title': 'Nasze realizacje',
            'description': 'Jesteś ciekaw co robimy? Sprawdź nasze wykonane systemy, a następnie skontaktuj się z nami.',
            'keywords': 'opole, kędzierzyn-koźle, krapkowice, gsm-monit',
        }
        return render(request, 'sites/web/realizacje.html', context)
