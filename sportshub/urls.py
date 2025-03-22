from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),  # This includes the URLs from the 'accounts' app
]
