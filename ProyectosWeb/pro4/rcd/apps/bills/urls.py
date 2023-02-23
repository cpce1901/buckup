from django.contrib import admin
from django.urls import path
from.views import TicketsList

app_name = 'bills_app'

urlpatterns = [
    path('tickets/', TicketsList.as_view(), name='tickets'),
]