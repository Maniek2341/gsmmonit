from django.shortcuts import render
from django.views import View


class UslugiSerwisoweView(View):
    def get(self, request):
        context = {
            'title': 'Usługi serwisowe',
            'description': 'Nie działa kamera lub jest brudna? Wykonujemy naprawy oraz czyszczenie kamer.',
            'keywords': 'serwisy monitoringów, opole, opolskie',
        }
        return render(request, 'sites/web/uslugi_serwisowe.html', context)
