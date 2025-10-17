from django.db import models
from django.contrib.auth.models import User

# ==============================
#  FOOD MODEL
# ==============================


class Food(models.Model):
    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("drink", "Drink"),
        ("snack", "Snack"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="food")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="foods/", blank=True, null=True)
    available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==============================
# ORDER MODEL
# ==============================
class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("delivered", "Delivered"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    date_ordered = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically calculate total price
        self.total_price = self.food.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


# ==============================
#  SUPPLY MODEL
# ==============================
class Supply(models.Model):
    STATUS_CHOICES = [
        ("on_time", "On Time"),
        ("delayed", "Delayed"),
        ("failed", "Failed"),
    ]

    supplier_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    expected_date = models.DateField()
    actual_date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="on_time")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} - {self.supplier_name}"
