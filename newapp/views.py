from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


def get_admin_url(request):
    return render(request, 'home.html')