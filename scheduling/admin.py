from django.contrib import admin
from .models import Booking, Availability
# Register your models here.
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'day_of_week', 'start_time', 'end_time', 'created_at')
    list_filter = ('specialist', 'day_of_week')
    search_fields = ('specialist__name',)

admin.site.register(Availability, AvailabilityAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'specialist', 'service', 'start_time', 'end_time', 'status', 'created_at')
    list_filter = ('specialist', 'service', 'status')
    search_fields = ('customer__name', 'specialist__name', 'service__name')

admin.site.register(Booking, BookingAdmin)