from django.shortcuts import render
from django.views import View


class KontrolaDostepuView(View):
    def get(self, request):
        context = {
            'title': 'Kontrola dostępu',
            'description': 'Wykonamy dla ciebie kontrole dostępu.',
            'keywords': 'kontrola dostępu, opole, opolskie',
        }
        return render(request, 'sites/web/kontrola_dostepu.html', context)
