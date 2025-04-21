from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from sportshub import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/live-scores/", views.get_live_scores, name="live-scores"),
    path("", views.home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),  # Login/Logout
    path("accounts/", include("users.urls")),  # Sign up
]
