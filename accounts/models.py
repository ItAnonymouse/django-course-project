from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Add related_name to avoid conflicts with auth.User.groups and auth.User.user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', 
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )
