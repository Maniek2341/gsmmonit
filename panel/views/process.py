# importing the necessary libraries
import io
import os
from io import BytesIO, StringIO

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# defining the function to convert an HTML file to a PDF file
class Render:



    @staticmethod
    def render(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = io.BytesIO()
     pdf = pisa.CreatePDF(io.BytesIO(html.encode("utf-8")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None