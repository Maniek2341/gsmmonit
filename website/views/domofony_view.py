from django.shortcuts import render
from django.views import View


class DomofonyView(View):
    def get(self, request):
        context = {
            'title': 'Domofony',
            'description': 'Dzięki nam zdalnie otworzysz brame lub furtkę bez wychodzenia z domu.',
            'keywords': 'domofony, bramy, opole, gsm-monit',
        }
        return render(request, 'sites/web/domofony.html', context)
