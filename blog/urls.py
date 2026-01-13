from django.urls import path

from .views import (
    HomeView,
    BlogsView,
    BlogDetailView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blogs/', BlogsView.as_view(), name='blogs'),
    path('blogs/<slug:title', BlogDetailView.as_view(), name='blog_detail'),
]
