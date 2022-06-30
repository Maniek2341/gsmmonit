from django.shortcuts import render
from django.views import View


class ONasView(View):
    def get(self, request):
        context = {
            'title': 'O nas',
            'description': 'Najważniejsze informacje o firmie GSM-monit.',
            'keywords': 'opole, opolskie, gsm-monit',
        }
        return render(request, 'sites/web/onas.html', context)
