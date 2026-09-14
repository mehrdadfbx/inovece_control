from rest_framework import viewsets

from .serializers import BusinessSerializer, ServiceSerializer, SpecialistSerializer,SpecialistServiceSerializer
from .models import Business, Service, Specialist, SpecialistService

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SpecialistViewSet(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

class SpecialistServiceViewSet(viewsets.ModelViewSet):
    queryset = SpecialistService.objects.all()
    serializer_class = SpecialistServiceSerializer