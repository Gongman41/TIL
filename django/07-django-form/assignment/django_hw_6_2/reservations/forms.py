from django import forms
from .models import Reservation

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     # model과 비슷, 차이 존재하긴 함

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        # 어떤 모델과 연동
        fields = '__all__'
        # 어떤 필드를 출력