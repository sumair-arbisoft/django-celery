from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    is_pitched = models.BooleanField(blank=True, null=True)
    is_pitched_at = models.DateField(blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.user.username
