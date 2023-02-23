from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Tickets

# Create your views here.
class TicketsList(ListView):
    template_name = 'bills/tickets.html'
    model = Tickets
    context_object_name = 'tickets'
    paginate_by = 50
