from django import forms
from .models import Diary_model


class DiaryForm(forms.ModelForm):

    class Meta:
        model = Diary_model
        fields = '__all__'
        # exclude = ('is_completed', )
        