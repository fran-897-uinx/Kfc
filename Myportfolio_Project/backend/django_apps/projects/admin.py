from django.contrib import admin
from .models import Project
 

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','github_link')
    list_filter = ("title",)
    search_fields = ['title', 'description']
    
    