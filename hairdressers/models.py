from django.db import models
from django.contrib.auth.models import User

class Hairdresser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    rating_avg = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

class Service(models.Model):
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    price = models.IntegerField()  # UGX
    duration_min = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Availability(models.Model):
    hairdresser = models.ForeignKey(Hairdresser, on_delete=models.CASCADE, related_name='availabilities')
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(7)])  # 0=Mon
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.hairdresser} - Day {self.day_of_week}"