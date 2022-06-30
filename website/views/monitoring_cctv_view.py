from django.shortcuts import render
from django.views import View


class MonitoringCCTVView(View):
    def get(self, request):
        context = {
            'title': 'Systemy monitoringu',
            'description': 'Zajmujemy się montażem monitoringu CCTV oraz GSM',
            'keywords': 'monitoring, monitoring cctv, monitoring gsm, kamery, rejestratory, opole',
        }
        return render(request, 'sites/web/monitoring_cctv.html', context)
