from django.contrib import admin
from .models import Inventory, Invoice, InventoryLog, InvoiceItem
# Register your models here.
class InvoceAdmin(admin.ModelAdmin):
    list_display  = ('user', 'status', 'order_date',)
    list_filter   = ('user', 'status',)
    search_fields = ('user', 'status',)
    ordering      = ('user',)

admin.site.register (Invoice, InvoceAdmin)

class InventoryAdmin(admin.ModelAdmin):
    list_display  = ('product', 'warehouse_location', 'quantity',)
    list_filter   = ('product', 'warehouse_location', 'quantity',)
    search_fields = ('product', 'warehouse_location', 'quantity')
    ordering      = ('warehouse_location',)

admin.site.register(Inventory, InventoryAdmin)


