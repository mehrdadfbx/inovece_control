from django.db import models

# Create your models here.
class Business(models.Model):
    owner = models.ForeignKey('users.Owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Service(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class SpecialistService(models.Model):
    specialist = models.ForeignKey('businesses.Specialist', on_delete=models.CASCADE)
    service = models.ForeignKey('businesses.Service', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.specialist.name} - {self.service.name}"


class Specialist(models.Model):
    business = models.ForeignKey('businesses.Business', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name