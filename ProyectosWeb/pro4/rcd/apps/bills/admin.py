from django.contrib import admin
from .models import Docuemnts, Tickets, Bills, Workers

# Register your models here.
class DocuemntsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')


class WorkersAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'position', 'total_boletas', 'total_facturas')

    def total_boletas(self, obj):
        result = Tickets.objects.filter(user = obj).count()
        return result
    
    def total_facturas(self, obj):
        result = Bills.objects.filter(user = obj).count()
        return result


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('user','type', 'date', 'rut', 'name', 'use', 'cash')
    list_filter = ('user', 'date')


class BillsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'rut', 'name', 'use', 'address', 'giro', 'total')
    list_filter = ('user','date')


admin.site.register(Docuemnts, DocuemntsAdmin)
admin.site.register(Workers, WorkersAdmin)
admin.site.register(Tickets, TicketsAdmin)
admin.site.register(Bills, BillsAdmin)