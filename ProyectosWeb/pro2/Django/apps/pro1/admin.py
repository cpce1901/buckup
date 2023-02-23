from django.contrib import admin
from . import models

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    ordering = ('id',)
    
    


admin.site.register(models.Extras)
admin.site.register(models.Payment, PaymentAdmin)
admin.site.register(models.Station)

