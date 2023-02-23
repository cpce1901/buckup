from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ReadPage(TemplateView):
    template_name = 'pro-2.html'