from django.db import models

class Diary_model(models.Model):
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)