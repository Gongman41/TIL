from django import forms

'''
둘다 class에 상속시켜줄 class라는 점
class -> PascalCase
Form vs ModelForm
Form -> Model에 대한 정보가 없는 Form을 위한 클래스
ModelForm -> Model에 대한 정보가 있는 Form을 위한 클래스
'''

class ArticleForm(forms.Form):
    # 모델에 대한 정보 없이 Form을 구성하려면?
    # 적절한 Fieldemfdmf sork wlrwjq wkrtjdgownjdigksek.
    '''
        django model정의하는 거랑 똑같
    '''
    title = forms.