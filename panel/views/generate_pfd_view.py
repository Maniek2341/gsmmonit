import json

import googlemaps
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse

from GSM import settings
from ..models import SerwisRaport


# Creating a class based view
class MyPDF(PDFTemplateView):
    template_name = "panel/pdf/serwis_pdf.html"

    def get(self, request, pk):
        raport = SerwisRaport.objects.get(pk=pk)

        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)

        calculate = json.dumps(gmaps.distance_matrix("Przysiecz Stawowa 2",
                                                     raport.firma.miejscowosc + raport.firma.ulica,
                                                     mode="driving"))

        calculate2 = json.loads(calculate)

        distance = calculate2['rows'][0]['elements'][0]['distance']['text']
        km = distance[:-2]
        obakierunki = (float(km) * 2)
        context = {
            'raport': raport,
            'dojazd': obakierunki
        }

        response = PDFTemplateResponse(request=request,
                                       template=self.template_name,
                                       filename="Serwis %s %s.pdf" % (raport.data_end, raport.firma.nazwa_firmy),
                                       context=context,
                                       show_content_in_browser=False,
                                       )
        return response
