from django.contrib import admin
from .models import Business, Service, Specialist, SpecialistService

# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','owner', 'created_at')
    list_filter = ('created_at', 'id')
    search_fields = ('name',)

admin.site.register(Business, BusinessAdmin)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','price', 'created_at')
    list_filter = ('created_at', 'id')
    search_fields = ('name',)

admin.site.register(Service, ServiceAdmin)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('created_at', 'id')
    search_fields = ('name',)

admin.site.register(Specialist, SpecialistAdmin)
class SpecialistServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'specialist', 'service')
    list_filter = ('specialist', 'service')
    search_fields = ('specialist__name', 'service__name')

admin.site.register(SpecialistService, SpecialistServiceAdmin)