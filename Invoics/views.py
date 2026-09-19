from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
        return [IsAuthenticatedOrReadOnly()]


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