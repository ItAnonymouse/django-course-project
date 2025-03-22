# accounts/views.py

from django.shortcuts import render

def login_view(request):
    # Add the logic for your login view here
    return render(request, 'accounts/login.html')
