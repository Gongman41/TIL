from django.db import models
# from accounts.models import User
#  django에서는 User모델을 직접참조하지않는다
from django.conf import settings
# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 문자열 반환. User면 객체
    #사용위치  settings.AUTH_USER_MODELS는 models.py에서만사용. 다른곳에선 get_user_model
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 외래키 값에대한 
    # 기본값 설정


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
