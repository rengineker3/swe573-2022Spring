from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='uploads/default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True, null=True)
    occupation = models.TextField(max_length=30, blank=True, null=True)
   

    



