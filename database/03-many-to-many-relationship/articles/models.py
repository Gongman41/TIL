from django.db import models
from django.conf import settings
# django에서는 User 모델을 '직접' 참조하지 않는다.
# from accounts.models import User


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 다대다는 복수형으로
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    # N:1에서의 역참조와 N:M에서의 역참조가 충돌. related 뭐시기로 다대다쪽을 바꿈
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
