# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Food, Order, Supply, user


@admin.register(user)
class Useradmin(admin.ModelAdmin):
    list_display = ("name", "email", "role")
    search_fields = ("role", "name")
    list_filter = ("name", "role")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'date_added')
    search_fields = ('name',)
    list_filter = ('category', 'available')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'quantity', 'total_price', 'status', 'date_ordered')
    list_filter = ('status', 'date_ordered')
    search_fields = ('user__username', 'food__name')

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'food_name', 'quantity', 'status', 'expected_date')
    list_filter = ('status',)
    search_fields = ('supplier_name', 'food_name')
