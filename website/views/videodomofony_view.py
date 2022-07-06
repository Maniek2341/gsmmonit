from django.shortcuts import render
from django.views import View


class VideoDomofonyView(View):
    def get(self, request):
        context = {
            'title': 'Videodomofony',
            'description': 'Chcesz zabezpieczyc dom? My wykonamy system alarmowy oraz bedziesz mógl nim sterowac za pomocą telefonu.',
            'keywords': 'videodomofony, opole, opolskie',
        }
        return render(request, 'sites/web/wideodomofony.html', context)
