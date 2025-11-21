from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import (
    Menu,
    Reservation,
    Student,
    GroupLink,
    Contact,
    GalleryItem,
    BlogDisplay,
)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuSerializer
from rest_framework import generics
from .forms import StudentForm, ReservationForm

# from django.http import HttpResponse, HttpResponseRedirect

# requirements for sending email----------------------
from django.template.loader import render_to_string
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.conf import settings
from datetime import datetime

# Create your views here.


def home(request):
    return render(request, "public.html")


def blog(request):
    response = requests.get(
        "https://www.themealdb.com/api/json/v1/1/filter.php?a=Canadian"
    )
    data = response.json()
    meals = data.get("meals", [])
    blogs = BlogDisplay.objects.all().order_by("created_at")

    context = {"meals": meals, "blogs": blogs}
    return render(request, "blog.html", context)


def blog_details(request, pk):
    blog = get_object_or_404(BlogDisplay, pk=pk)

    return render(request, "blog_details.html", {"blog": blog})


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("description")
        if not all([name, email, desc]):
            return render(
                request,
                "contact.html",
                {"error": "All fields are required, please."},
            )
        contact_details = Contact.objects.create(name=name, email=email, desc=desc)
        html_content = render_to_string(
            "contact_email.html",
            {"name": name, "email": email, "desc": desc},
        )
        subject = "Contact Form Submission Received"
        text_content = f"""
        Hello {name},
        Thank you for reaching out to us. We have received your message and will get back to you shortly.
        Here is a summary of your submission:
        """
        from_email = [email]
        recipient_list = settings.DEFAULT_FROM_EMAIL

        email = EmailMultiAlternatives(
            subject, text_content, from_email, to=recipient_list
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)

        return render(
            request, "contactsuccess.html", {"contact_details": contact_details}
        )
    return render(request, "contact.html")


# @api_view(["GET", "POST", "PUT", "DELETE"])
def menu(request, category=None):
    menus = Menu.objects.all()

    category_filter = request.GET.get("category")
    if category_filter in ["food", "drink", "snack"]:
        menus = menus.filter(selection=category_filter)

    context = {"menus": menus, "active_category": category_filter}
    return render(request, "menu.html", context)


def reservation_view(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Save the reservation
            reservation = form.save()

            # Extract data from the saved reservation
            name = reservation.name
            email = reservation.email
            date = reservation.date
            number = reservation.guest_phone_num
            description = reservation.meassage
            menu_items = reservation.menu_items.all()

            # -------------------------
            # Customer Email
            # -------------------------
            html_content = render_to_string(
                "reservation/emails/reservation_email.html",
                {
                    "reservation": reservation,
                    "menu_items": menu_items,
                },
            )
            subject = "Your Table Reservation Has Been Received"
            text_content = f"""
            Hello {name},

            Your table reservation has been received. You will receive a call shortly.
            Date: {date}

            We look forward to having you dine with us.

            - The KFC Team
            """
            customer_email = EmailMultiAlternatives(
                subject, text_content, settings.DEFAULT_FROM_EMAIL, [email]
            )
            customer_email.attach_alternative(html_content, "text/html")
            customer_email.send(fail_silently=False)

            # -------------------------
            # Owner Email
            # -------------------------
            owner_html = render_to_string(
                "reservation/emails/reservation_email_owner.html",
                {
                    "reservation": reservation,
                    "menu_items": menu_items,
                },
            )
            owner_email = EmailMultiAlternatives(
                "📩 New Reservation Received",
                "",
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],  # Or your actual owner email(s)
            )
            owner_email.attach_alternative(owner_html, "text/html")
            owner_email.send(fail_silently=False)

            return render(
                request,
                "reservation/reservation_success.html",
                {"reservation": reservation},
            )

    else:
        form = ReservationForm()
    return render(request, "reservation.html", {"form": form})


def gallery(request):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
    data = response.json()
    meals = data.get("meals", [])
    items = GalleryItem.objects.all().order_by("-created_at")

    context = {"meals": meals, "items": items}
    return render(request, "gallery.html", context)


def food_list(request):
    foods = Menu.object.filter(selection="food")
    return render(request, "menu.html", {"foods": foods})


def drink_list(request):
    drinks = Menu.object.filter(selection="drink")
    return render(request, "menu.html", {"drinks": drinks})


def snack_list(request):
    snack = Menu.object.filter(selection="snack")
    return render(request, "menu.html", {"snack": snack})


def student_registration(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()

            # Extract details
            name = student.name
            email = student.email
            phone_number = student.phone_number
            reason = student.reason
            date = student.registered_on

            # Render email templates
            html_content = render_to_string(
                "studentsemail.html",
                {"student": student, "year": datetime.now().year},
            )

            text_content = f"""
            Hello {name},

            We are glad you have joined us as a student at KFC Restaurant!

            Date: {date}

            We look forward to communicating with you soon.

            -- The KFC Team
            """

            subject = "You Have Successfully Registered as a Student at KFC Restaurant"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            msg = EmailMultiAlternatives(
                subject, text_content, from_email, recipient_list
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # ✅ Check for active WhatsApp group
            group = GroupLink.objects.filter(active=True).first()

            if group and group.link:
                student.joined_group_name = group
                student.whatsapp_joined = True
                student.save()
                # ✅ Redirect immediately to WhatsApp group
                return redirect(group.link)

            # ❌ If no active group, show success page with message
            return render(
                request,
                "studentsuccess.html",
                {
                    "student": student,
                    "message": "Registration successful, but no active group found.",
                    "whatsapp_group": None,
                },
            )

    else:
        form = StudentForm()

    return render(request, "studentForm.html", {"form": form})
