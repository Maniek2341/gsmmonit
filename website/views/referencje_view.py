from django.shortcuts import render
from django.views import View


class ReferencjeView(View):
    def get(self, request):
        context = {
            'title': 'Referencje',
            'description': 'Zobacz referencje od naszych klientów.',
            'keywords': '',
        }
        return render(request, 'sites/web/referencje.html', context)
