from django.shortcuts import render, redirect
import requests
from .models import Menu, Reservation, Student, GroupLink
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MenuSerializer
from rest_framework import generics
from .forms import StudentForm

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

    context = {"meals": meals}
    return render(request, "blog.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


@api_view(["GET", "POST", "PUT", "DELETE"])
def menu(request, id=None):
    menus = Menu.objects.all()
    if request.method == "GET":
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    elif request.method == "PUT":
        menus = Menu.objects.get(id=id)
        serializer = MenuSerializer(menus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "POST":
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        menus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def reservation_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("date")
        number = request.POST.get("guest_phone_num")
        description = request.POST.get("message")

        if not all([name, email, date, number, description]):
            return render(
                request,
                "reservation.html",
                {"error": "All fields are required, please."},
            )

        # Save reservation
        reservation = Reservation.objects.create(
            name=name,
            email=email,
            date=date,
            guest_phone_num=number,
            meassage=description,
        )

        html_content = render_to_string(
            "reservation/emails/reservation_email.html",
            {
                "name": name,
                "email": email,
                "date": date,
                "guest_phone_num": number,
                "description": description,
            },
        )

        # Send confirmation email
        subject = "Your Table Reservation Has Been Received"
        text_content = f"""
        Hello {name},
        Your table reservation has been received. You will receive a call shortly.
        Date: {date}
        We look forward to having you dine with us.
        
        - The KFC Team
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [reservation.email]

        email = EmailMultiAlternatives(
            subject, text_content, from_email, to=recipient_list
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)

        return render(
            request,
            "reservation/reservation_success.html",
            {"reservation": reservation},
        )

    return render(request, "reservation.html")


def gallery(request):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=")
    data = response.json()
    meals = data.get("meals", [])

    context = {"meals": meals}
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
