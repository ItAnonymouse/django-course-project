from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your custom user model in the admin
admin.site.register(CustomUser, UserAdmin)
