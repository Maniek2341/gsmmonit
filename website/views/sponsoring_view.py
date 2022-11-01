from django.shortcuts import render
from django.views import View


class SponsoringView(View):
    def get(self, request):
        context = {
            'title': 'Sponsoring',
            'description': 'Oferujemy wykonanie wizyjnego monitoringu twojej budowy!',
            'keywords': 'monitoring gsm, monitoring budowy, opole, opolskie',
        }
        return render(request, 'sites/web/sponsoring.html', context)
