from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor


# Create your views here.
class AutorList(ListView):
    template_name = 'autor/list.html'    
    context_object_name = 'lista_autores'

    def get_queryset(self):  
        clave = self.request.GET.get('Kword',)      
        return Autor.objects.Filtro_name(clave)