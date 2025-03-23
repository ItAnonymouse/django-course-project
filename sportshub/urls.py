from django.contrib import admin
from django.urls import path, include
from sportshub import views  # ✅ Make sure 'views.py' exists in sportshub

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # ✅ This should work
    path('accounts/', include('accounts.urls')),
]
