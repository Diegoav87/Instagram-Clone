from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField()
    likes = models.IntegerField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.quote

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.text


