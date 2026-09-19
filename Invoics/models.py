from django.db import models


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
    order_date = models.DateField()
    order_time = models.TimeField()
    note = models.TextField(blank=True, null=True)
    reviewed_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_invoices')
    reviewed_at = models.DateTimeField(null=True, blank=True)
    admin_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='invoice_items')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=14, decimal_places=2)
    subtotal = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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