from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    nickname = models.CharField(max_length=30)
    followings = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles'
    )