from django.shortcuts import render
from django.views import View


class RCPView(View):
    def get(self, request):
        context = {
            'title': 'Systemy RCP',
            'description': 'Oferujemy wykonanie wizyjnego monitoringu twojej budowy!',
            'keywords': 'monitoring gsm, monitoring budowy, opole, opolskie',
        }
        return render(request, 'sites/web/rcp.html', context)
