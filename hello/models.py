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


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Ссылка на владельца (пользователя)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)  # Ссылка на объект (оружие)
    quantity = models.PositiveIntegerField(default=1)  # Количество оружия в корзине

    def __str__(self):
        return f"{self.user.username}'s cart: {self.quantity} x {self.weapon.name}"
