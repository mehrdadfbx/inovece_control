from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('paid', 'Paid'),
    ]

    invoice_number = models.CharField(max_length=30, unique=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='invoices')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2)
    order_date   = models.DateField()
    order_time   = models.TimeField()
    note         = models.TextField(blank=True, null=True)
    reviewed_by  = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_invoices')
    reviewed_at  = models.DateTimeField(null=True, blank=True)
    admin_note   = models.TextField(blank=True, null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            last = Invoice.objects.order_by('id').last()
            next_id = (last.id + 1) if last else 1
            self.invoice_number = f"INV-{timezone.now().year}-{next_id:06d}"
        super().save(*args, **kwargs)

    def recalculate_total(self):
        result                    = self.items.aggregate(total=Sum('subtotal')) 
        total                     = result.get('total') or 0
        self.total_amount         = total 
        self.save(update_fields   =['total_amount'])




class InvoiceItem(models.Model):
    invoice    = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product    = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='invoice_items')
    quantity   = models.IntegerField()
    unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    subtotal   = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        self.invoice.recalculate_total()        

    def delete(self, *args, **kwargs):
        invoice = self.invoice   # قبل از حذف نگهش دار
        super().delete(*args, **kwargs)
        invoice.recalculate_total()
class InventoryLog(models.Model):
    CHANGE_TYPE_CHOICES = [
        ('in', 'In'),
        ('out', 'Out'),
        ('adjustment', 'Adjustment'),
    ]
    REFERENCE_TYPE_CHOICES = [
        ('invoice', 'Invoice'),
        ('manual', 'Manual'),
        ('return', 'Return'),
    ]

    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='inventory_logs')
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPE_CHOICES)
    quantity_change = models.IntegerField()
    reference_type = models.CharField(max_length=20, choices=REFERENCE_TYPE_CHOICES)
    reference_id = models.BigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_inventory_logs')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['reference_type', 'reference_id']),
        ]


class Inventory(models.Model):
    product = models.OneToOneField('products.Product', on_delete=models.CASCADE, related_name='inventory')
    quantity = models.IntegerField(default=0)
    min_stock_level = models.IntegerField(default=0)
    warehouse_location = models.CharField(max_length=100, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)