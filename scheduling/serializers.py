from rest_framework import serializers
from .models import Availability, Booking

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['specialist', 'day_of_week', 'start_time', 'end_time']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['customer', 'specialist', 'service', 'start_time', 'end_time', 'status']