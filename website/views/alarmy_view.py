from django.shortcuts import render
from django.views import View


class AlarmyView(View):
    def get(self, request):
        context = {
            'title': 'Systemy alarmowe',
            'description': 'Chcesz zabezpieczyc dom? My wykonamy system alarmowy oraz bedziesz mógl nim sterowac za pomocą telefonu.',
            'keywords': 'alarm, system alarmowy, opole',
        }
        return render(request, 'sites/web/alarmy.html', context)
