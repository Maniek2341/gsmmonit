from django.shortcuts import render
from django.views import View


class ElektrykaView(View):
    def get(self, request):
        context = {
            'title': 'Instalacje elektryczne',
            'description': 'Wykonujemy instalacje elektryczne na najwyższym poziomie.',
            'keywords': 'elektryka, instalacje elektryczne, opole, prószków',
        }
        return render(request, 'sites/web/elektryka.html', context)
