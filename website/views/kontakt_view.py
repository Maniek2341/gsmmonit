from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View

from GSM.settings import DEFAULT_FROM_EMAIL
from website.forms import ContactForm


class KontaktView(View):
    def get(self, request):
        context = {
            'title': 'Skontaktuj sie z nami',
            'kontakt': ContactForm(),
            'description': 'Nie czekaj tylko skontaktuj sie z nami.',
            'keywords': '',
        }
        return render(request, 'sites/web/kontakt.html', context)

    def post(self, request):
        contact_form = ContactForm(request.POST)

        context = {
            'contact': contact_form
        }

        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            mail_content = {
                'imie': form.imie,
                'email': form.email,
                'temat': form.temat,
                'phone': form.phone,
                'tresc': form.tresc,
            }
            form.save()

            message = render_to_string('sites/mail/contact.html', mail_content)

            send_mail(
                subject=form.temat,
                message='',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=['damianpielka@o2.pl'],
                fail_silently=True,
                html_message=message
            )

            return HttpResponseRedirect(reverse_lazy("kontakt"))
