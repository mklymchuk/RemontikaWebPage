"""Defines URL patterns for company."""

from django.urls import path

from . import views

app_name = 'company'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Page that show all services.
    path('service/', views.services, name='service'),
]
