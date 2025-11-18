from django.urls import path
from . import views

urlpatterns = [
    path("", views.users_record, name="users_record"),
    path("ordered_record/", views.ordered_record, name="ordered_record"),
    path("pending_record/", views.pending_record, name="pending_record"),
    path("failed_record/", views.failed_record, name="failed_record"),
    path("upload-gallery/", views.upload_gallery, name="upload_gallery"),
    path("upload_blog/", views.upload_blog, name="upload_blog"),
    path("upload_menu/", views.upload_menu, name="upload_menu"),
]
