from rest_framework import viewsets

from .serializers import AvailabilitySerializer, BookingSerializer
from .models import Availability, Booking
# Create your views here.

class availabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class bookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer