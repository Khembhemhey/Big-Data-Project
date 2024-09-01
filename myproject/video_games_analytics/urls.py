from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns here
    path('', views.index, name='index'),
    path('analytics/', views.analytics, name='analytics'),
    # Add more URL patterns as needed
]
