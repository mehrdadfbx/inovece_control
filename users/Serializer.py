from rest_framework import serializers
from users.models import Owner, Customer

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['name','phone_number',]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number',]
        