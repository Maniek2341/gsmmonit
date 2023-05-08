from django.contrib import messages
from django.contrib.auth import authenticate, login
import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from panel.forms import LoginForm


class LoginView(View):
    def get(self, request):
        context = {
            'login_form': LoginForm()
        }
        return render(request, 'panel/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                messages.info(request, json.dumps(
                    {
                        'body': "Pomyślnie zalogowano jako %s" % username,
                        'title': "Zalogowano!"
                    }
                ))

                return HttpResponseRedirect(reverse_lazy("dashboard"))
            else:
                messages.error(request, json.dumps(
                    {
                        'body': "Twój login lub hasło są nieprawidłowe, spróbuj ponownie!",
                        'title': "Brak autoryzacji!"
                    }
                ))

            context = {
                'login_form': form
            }
            return render(request, "panel/login.html", context)