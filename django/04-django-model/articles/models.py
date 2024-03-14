from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 필드이름 , 데이터 타입
    # 최종 테이블 이름은 앱이름_모델클래스 이름
# Create your models here.
