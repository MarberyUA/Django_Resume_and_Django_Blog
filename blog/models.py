from django.db import models
from Resume_Engine.settings import AUTH_USER_MODEL


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class LikeAction(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='likes')
    press_like = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username