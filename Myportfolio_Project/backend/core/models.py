from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    hero_image = models.ImageField(upload_to="home/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    profile_image = models.ImageField(upload_to="about/", blank=True, null=True)
    tech_stack = models.JSONField(default=list, blank=True)  # e.g. ["Next.js", "Django", "Tailwind"]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class Testimonails(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    avatar = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

# backend/apps/services/models.py
class Service(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Bootstrap or Heroicon name")
    description = models.TextField()

    def __str__(self):
        return self.title
