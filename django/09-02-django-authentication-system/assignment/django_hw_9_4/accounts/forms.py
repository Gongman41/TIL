from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from models import User 직접참조하면 문제발생가능
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # 현재 django 프로젝트에 활성화된 User 객체를 반환하는 함수.

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name')
        # 비밀번호 변경은 다른 form 사용