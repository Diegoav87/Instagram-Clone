from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, default='default_pic.jpg')
    bio = models.TextField(blank=True, default='')

    def __str__(self):
        return self.user.username

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='followed_users')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', blank=True, null=True)

    def __str__(self):
        return self.user.username


    

