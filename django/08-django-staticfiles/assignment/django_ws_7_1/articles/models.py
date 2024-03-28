from django.db import models
# def 미디어파일 상세경로 

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True,upload_to='%Y/%m/%d/')
    image_description = models.TextField()
    content = models.CharField(max_length=250)
    # 늦게 추가했기때문에 애초에 맨 오른쪽. 빈 값 도 허용
    # 이미지필드 라이브러리 필수
    # upload_to= 빈 값이 디폴트.
    # 업로드 날짜로 %Y/%m/%d/
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default = True)