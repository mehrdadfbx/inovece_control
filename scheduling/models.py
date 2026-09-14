from django.db import models

# Create your models here.
class Availability(models.Model):
    specialist = models.ForeignKey('businesses.Specialist', on_delete=models.CASCADE)
    day_of_week = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(7)])  # 0=Monday, 6=Sunday
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.specialist.name} - {self.day_of_week} ({self.start_time} - {self.end_time})"

class Booking(models.Model):
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE)
    specialist = models.ForeignKey('businesses.Specialist', on_delete=models.CASCADE)
    service = models.ForeignKey('businesses.Service', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.customer.name} - {self.specialist.name} - {self.service  .name} at {self.start_time}"