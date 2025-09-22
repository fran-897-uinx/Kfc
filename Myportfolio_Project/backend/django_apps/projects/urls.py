from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('<int:id>/', views.ProjectDetailView.as_view(), name='project-detail'),
]