from itertools import product
from urllib import request

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from users.permissions import IsAdminRole
from .serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
    InventoryLogSerializer,
    InventorySerializer,
)


from .models import Invoice, InvoiceItem, InventoryLog, Inventory


class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminRole()]
        return [IsAuthenticated()]

    def perform_create(self,serializer):
        product =  serializer.validate_data['product']
        serializer.save(unit_price=product.price)


    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        invoce = self.get_object()
        return Response({"status": "totall update"})
    


class InvoiceItemViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceItemSerializer
    queryset = InvoiceItem.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminRole()]
        return [IsAuthenticatedOrReadOnly()]


class InventoryLogViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryLogSerializer
    queryset = InventoryLog.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminRole()]
        return [IsAuthenticatedOrReadOnly()]


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminRole()]
        return [IsAuthenticatedOrReadOnly()]