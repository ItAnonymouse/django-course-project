from django.contrib import admin
from django.urls import path
from sportshub import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/football/scheduled-events/<str:date>/", views.get_scheduled_football_events, name="scheduled-football-events"),
    path("", views.home, name="home"),  # Home page with the welcome message
]
