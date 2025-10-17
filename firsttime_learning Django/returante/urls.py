from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.shortcuts import render, redirect

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("gallery/", views.gallery, name="gallery"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("menu/<int:id>", views.menu, name="menu"),
    path("Registeration/", views.student_registration, name="student"),
    path("reservation", views.reservation_view, name="reservation"),
    path("", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "student/success/",
        lambda request: render(
            request,
            "studentsuccess.html",
        ),
        name="student_success",
    ),
]


# urlpatterns = format_suffix_patterns(urlpatterns)
