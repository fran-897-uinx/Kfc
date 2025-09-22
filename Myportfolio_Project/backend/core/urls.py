from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("testimonials/", views.TestimonailsView.as_view(), name="testimonials"),
    path("services/", views.ServicesView.as_view(), name="services"),
]
