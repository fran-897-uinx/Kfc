from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path("external-blogs/", views.ExternalBlogView.as_view(), name="external-blogs"),

]
