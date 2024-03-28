from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_hidden = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
# DB동작과 python object 동작 구분짓기
    def __str__(self):
        return f'{self.pk}번째 게시글 {self.title}'
    