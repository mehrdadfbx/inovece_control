from rest_framework import serializers
from .models import Business, Service, Specialist, SpecialistService 

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['name', 'address', 'phone_number']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'duration_minutes', 'price']


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['name', 'phone_number']


class SpecialistServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialistService
        fields = ['specialist', 'service']



