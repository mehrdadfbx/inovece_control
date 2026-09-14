from rest_framework import viewsets

from .Serializer import OwnerSerializer, CustomerSerializer
from users.models import Owner, Customer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer