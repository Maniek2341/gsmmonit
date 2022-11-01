from django.shortcuts import render
from django.views import View


class UslugiDodatkoweView(View):
    def get(self, request):
        context = {
            'title': 'Usługi dodatkowe',
            'description': 'Oferujemy wykonanie wizyjnego monitoringu twojej budowy!',
            'keywords': 'monitoring gsm, monitoring budowy, opole, opolskie',
        }
        return render(request, 'sites/web/uslugi_dodatkowe.html', context)
