from django.db import models
from django.contrib.auth.models import User
from ..blog.models import Post


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return self.user.username

