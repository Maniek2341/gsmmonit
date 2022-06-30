from django.shortcuts import render
from django.views import View


class CertyfikatyView(View):
    def get(self, request):
        context = {
            'title': 'Certyfikaty',
            'description': 'Jesteśmy wykwalifikowaną firmą montującą kamery, alarmy oraz inne systemy.',
            'keywords': '',
        }
        return render(request, 'sites/web/certyfikaty.html', context)
