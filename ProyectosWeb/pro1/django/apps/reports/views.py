from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

# Create your views here.
class Report(LoginRequiredMixin, TemplateView):
    template_name = 'reports/report.html'
    login_url = reverse_lazy('users_app:login')