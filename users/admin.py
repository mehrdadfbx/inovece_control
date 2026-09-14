from django.contrib import admin
from .models import Owner, Customer
# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'created_at')
    list_filter = ('created_at', 'id')
    search_fields = ('name',)

admin.site.register(Owner, OwnerAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'created_at')
    list_filter = ('created_at', 'id')
    search_fields = ('name',)

admin.site.register(Customer, CustomerAdmin)