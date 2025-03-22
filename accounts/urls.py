# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # Add other URL patterns as necessary
]
