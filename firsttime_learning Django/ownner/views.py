from django.shortcuts import render
from .models import Food, Order, Supply
from returante.models import GalleryItem, BlogDisplay, Menu
from django.shortcuts import redirect
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


def upload_gallery(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("image")

        if name and image:
            GalleryItem.objects.create(name=name, image=image)

        return redirect("gallery")

    return render(request, "upload_gallery.html")


def upload_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        sub_title = request.POST.get("subtitle")
        image = request.FILES.get("image")
        description = request.POST.get("description")

        if title and description and image:
            BlogDisplay.objects.create(
                title=title, image=image, description=description, sub_title=sub_title
            )
        redirect("blog")

    return render(request, "upload_blog.html")


def upload_menu(request):
    if request.method == "POST":
        title = request.POST.get("title")
        discription = request.POST.get("discription")
        price = request.POST.get("price")
        sample = request.FILES.get("image")
        selection = request.POST.get("selection")
        if title and discription and sample and price and selection:
            Menu.objects.create(
                title=title,
                sample=sample,
                discription=discription,
                price=price,
                selection=selection,
            )
        redirect("menu")
    Menus = Menu.objects.all()
    context = {"Menus": Menus}
    return render(request, "upload_menu.html", context=context)
