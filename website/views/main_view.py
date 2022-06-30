from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        context = {
            'title': 'Monitoring, Alarmy, Domofony',
            'description': 'GSM-monit - Chcesz zamontować monitoring lub alarm? Dobrze trafiłeś zajmujemy sie systemami monitoringu i alarmu. Zajmujemy się dodatkowo instalacjami sieciowymi i elektrycznymi oraz domofonami i automatyką.',
            'keywords': 'Monitoring, Alarmy, Kamery, Domofony, Sieci, Elektryka, Opolskie, opole, województwo opolskie, gsm-monit, krapkowice, gogolin, kędzierzyn, koźle, prudnik, prószków',
        }
        return render(request, 'sites/web/main.html', context)
