from django.urls import path
from . import views

urlpatterns = [
    path("", views.users_record, name="users_record"),
    path("ordered_record/", views.ordered_record, name="ordered_record"),
    path("pending_record/", views.pending_record, name="pending_record"),
    path("failed_record/", views.failed_record, name="failed_record"),
]
