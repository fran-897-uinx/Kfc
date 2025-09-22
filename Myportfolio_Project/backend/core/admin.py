from django.contrib import admin
from .models import Home, About,Testimonails,Service

# Register your models here.

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    list_filter = ("title",)
    search_fields = ['title', 'created_on']
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    list_filter = ("heading",)
    search_fields = ['heading', 'created_on']
    
@admin.register(Testimonails)
class TestimonailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'testimonial')
    list_filter = ("name",)

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title",)
    search_fields = ['name', 'created_on']