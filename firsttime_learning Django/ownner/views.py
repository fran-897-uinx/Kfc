from django.shortcuts import render
from .models import Food, Order, Supply
from django.contrib.auth.decorators import user_passes_test
# Create your views here.

@user_passes_test(lambda u: u.is_staff)
def users_record(request):
    from django.contrib.auth.models import User
    users = User.objects.all()
    return render(request, 'records/users.html', {'users': users})

def ordered_record(request):
    orders = Order.objects.filter(status='delivered')
    return render(request, 'records/ordered.html', {'orders': orders})

def pending_record(request):
    pending_orders = Order.objects.filter(status='pending')
    return render(request, 'records/pending.html', {'pending_orders': pending_orders})

def failed_record(request):
    failed_supplies = Supply.objects.filter(status='failed')
    return render(request, 'records/failed.html', {'failed_supplies': failed_supplies})

