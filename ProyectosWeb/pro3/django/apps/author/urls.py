from django.contrib import admin
from django.urls import path
from . import views

name_app = 'author_app'

urlpatterns = [
    path('autores/', views.AutorList.as_view(), name='autores'),
]