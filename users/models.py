from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name




class Customer(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name