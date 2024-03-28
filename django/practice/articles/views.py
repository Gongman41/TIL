from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def create(request):
    # 생성을 위한 요청은 2가지 작업이 필요
    '''
    1. 생성하기 위한 데이터를 입력할 수 있는 페이지
    2. 입력한 데이터를 토대로 실제로 데이터를 생성하는 함수

    '''
    if request.method == 'POST':
        pass
        # POST 요청이 올려면 GET이 먼저다
    else:
        pass