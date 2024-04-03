from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    #on_delete 게시물 지워지면 댓글도 지우기. 외래키는 작성위치 상관ㅅ없이 테이블필드 마지막에 생성
    # 클래스 변수명_id 로 외래키 생성. 게시물 존재해야되고 NULL값 들어갈 수 없음.
    # 외래키를 통해 원래 게시물 접근 가능
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    