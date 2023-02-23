from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from apps.sensors.models import Variable, Sensor

import json

# Create your views here.
class Chart(LoginRequiredMixin, TemplateView):
    template_name = 'chart/chart.html'
    login_url = reverse_lazy('users_app:login')
    model = Variable
    context_object_name = 'data'
    
  
        

    def get_data(self, pedido):
        f1 = self.request.GET.get('kword1','')  #VAriable fecha 1 desde el fron
        f2 = self.request.GET.get('kword2','')  #VAriable fecha 2 desde el fron
        s = self.request.GET.get('kword3','')  #VAriable numero de sensor desde el fromn
        variable = self.request.GET.get('kword4','')   #VAriable electrica seleccionada 
      
        if f1 and f2 and s and variable:            
            d1=datetime.strptime(f1, '%Y-%m-%d').date()
            d2=datetime.strptime(f2, '%Y-%m-%d').date()    
            if pedido == 'v':   
                variable_envio = Variable.objects.filter(created__range = (d1, d2), sensor_id= s).values(variable)
                variable_envio = [i[variable] for i in variable_envio]
                print(variable_envio)
                return variable_envio   
            elif pedido == 'f':
                fecha = Variable.objects.filter(created__range = (d1, d2), sensor_id= s).values('created') 
               
                fecha = [str(i['created']) for i in fecha]
                print(fecha)
                return fecha
        
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(Chart, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Baklawa
        fields = Variable._meta.get_fields()
        list_fields = [field.get_attname_column()[1] for field in fields]
        list_fields = [i for i in list_fields if not i == 'id' and not i == 'created' and not i == 'sensor_id']    
        context['medidas'] = list_fields
        context['sensores'] = Sensor.objects.all()  
        context['data_variable'] = self.get_data('v')
        context['data_fecha'] = self.get_data('f')
                   
        return context
      
