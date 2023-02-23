from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Extras, Station, Payment

import requests

# Create your views here.
class Apiexternal(TemplateView):
    template_name = 'pro-1.html'  

    def save_Payment(self, data):
        payment_list = []
        name_payment = []
        
        data = data['network']
        data_sta = data['stations']
        for i in data_sta:
            payment = ( i['extra']['payment'])
            for pa in payment:
                if pa not in name_payment:                  
                    name_payment.append(pa)
        
        for i in name_payment:
            if Payment.objects.filter(method_pay = i):
                break
            else:
                pay = Payment(method_pay = i)
                payment_list.append(pay)
        
        if payment_list:            
            Payment.objects.bulk_create(payment_list)  
     

    def save_Extra(self, data):
        extra_list = []    
        pay_dic = {}
        
        data = data['network']
        data_sta = data['stations']        
                
        for i in data_sta:          

            try:
            
                extra = Extras(
                    addres = i['extra']['address'],
                    altitude = i['extra']['altitude'],
                    ebikes = i['extra']['ebikes'],
                    has_ebikes = i['extra']['has_ebikes'],
                    last_update = i['extra']['last_updated'],
                    normal_bikes = i['extra']['normal_bikes'],           
                    payment_terminal = i['extra']['payment-terminal'],
                    post_code = i['extra']['post_code'],
                    renting = i['extra']['renting'],
                    returning = i['extra']['returning'],
                    slot = i['extra']['slots'],
                    uid = i['extra']['uid'],
                )

                extra_list.append(extra)              
               

            except Exception:
                pass
                
               
        Extras.objects.bulk_create(extra_list)

        def cambio(lista):
            change_lista = []
            for i in lista:
                if i == 'key':
                    change_lista.append(1)
                elif i == 'transitcard':
                    change_lista.append(2)
                elif i == 'creditcard':
                    change_lista.append(3)
                elif i == 'phone':
                    change_lista.append(4)
            
            return change_lista

        for i in data_sta:          

            try:           
                key = i['extra']['uid']
                dato = i['extra']['payment']
                pay_dic[key] = cambio(dato)
                

            except Exception:
                pass

       
        for key, value in pay_dic.items():            
            print(key, value)
            for i in value:
                try:
                    Extras.objects.get(uid = key).payment.add(i)
                except Exception:
                    pass

    
    def get_data_api(self):
        url = 'http://api.citybik.es/v2/networks/bikesantiago'
        response = requests.get(url)
        data = response.json()    
        self.save_Payment(data)  
        self.save_Extra(data)         
        return data        
   
    
    def get_context_data(self, **kwargs):
        context = super(Apiexternal, self).get_context_data(**kwargs)      
        data_api = self.get_data_api()        
        return context
    

       
        
    