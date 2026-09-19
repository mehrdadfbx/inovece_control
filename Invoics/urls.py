from rest_framework.routers import DefaultRouter
from .views import (
    InvoiceViewSet,
    InvoiceItemViewSet,
    InventoryLogViewSet,
    InventoryViewSet,
)

router = DefaultRouter()
router.register('invoice', InvoiceViewSet, basename='invoice')
router.register('invoice-items', InvoiceItemViewSet, basename='invoiceitem')
router.register('inventory-logs', InventoryLogViewSet, basename='inventorylog')
router.register('inventory', InventoryViewSet, basename='inventory')

urlpatterns = router.urls