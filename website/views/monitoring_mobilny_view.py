from django.shortcuts import render
from django.views import View


class MonitoringMobilnyView(View):
    def get(self, request):
        context = {
            'title': 'Monitoring mobilny',
            'description': 'Oferujemy wykonanie wizyjnego monitoringu twojej budowy!',
            'keywords': 'monitoring gsm, monitoring budowy, opole, opolskie',
        }
        return render(request, 'sites/web/monitoring_mobilny.html', context)
