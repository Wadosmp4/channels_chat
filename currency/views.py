from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Currency


class CoinView(TemplateView):
    template_name = "currency/index.html"

    def get(self, request):
        currencies = Currency.objects.all()

        return render(request, 'currency/index.html', {'currencies': currencies})
