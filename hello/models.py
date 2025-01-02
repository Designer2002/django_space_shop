from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)  # Определяем, админ это или нет
    class Meta:
        app_label = 'hello' 
    def __str__(self):
        return self.username

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    power_consumption = models.CharField(max_length=50)
    charging_method = models.CharField(max_length=50)
    range = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    warranty = models.CharField(max_length=50)

    def __str__(self):
        return self.name
