웹페이지 과정
-  클라이언트가 주소 입력 -> 브라우저는 서버에 html파일 달라고 요청 -> 서버는 데이터베이스에서 파일을 찾아 응답-> 브라우저가 전달받은 html 해석해서 사용자는 메인페이지 보게됨
## Framework
- 웹어플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
- django framework: 파이썬기반의 대표적인 웹 프레임워크
 - 서버구축

## 가상환경
- python 어플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 독립적인 실행환경
  - 지금까지는 전역환경에 설치. 버전문제, 패키지 간 충돌 발생
- 명령어
  - python -m venv(가상환경 만들기) venv(가상환경이름)
    이 파일은 보통 개발하는 환경에 두는 게 일반적. 근데 다른 곳에 놔도 온오프하는 데에는 문제가 없다
    파일은 직접적으로 수정 절대 x
  - source venv/Scripts/activate
  - 각 gitbash에서 다른 환경 on off 가능
  - pip list: 설치된 패키지 확인
  - 패키지간 의존성 문제_ 가상환경에 대한 정보, 패키지 목록이 공유되어야 한다_ 원격저장소에는 가상환경 파일을 올리지 않기때문
  - pip freeze >(문자열을 쓰겠다) requirements(다른이름 가능하긴 한데 그냥 이렇게 고정).txt
  - .git 같은 건가

## Django
- 가상환경 생성
-  가상환경 활성화
- Django 설치_ pip install django
- 의존성 파일 생성(패키지 설치시마다 진행)
- django-admin startproject fistpjt .(온점 붙이면 바로 폴더로 이동. 현재 위치를 프로젝트화 하겠다)
- 서버 실행_ python manage.py runserver

- .gitignore 파일생성(django 넣으면 가상환경도 같이 들어감)
- git 저장소 생성
- django 프로젝트 생성

- LTS: 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용.

## 디자인 패턴
-  소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
- 애플리케이션 구조는 이렇게 구성하자_ 라는 관행
- MVC 디자인 패턴(모델_데이터, 뷰_사용자와 상호작용, 콘트롤_중간부분)
  - 독립적이고 쉽게 유지 보수할 수 있는 구조
- MTV 디자인 패턴(모델, 템플릿, 뷰) 똑같음

## 프로젝트와 앱
- 큰 프로젝트(전체 설정)에 각각의 기능이 구현된 앱(단위모듈)이 포함
- 개념상. 물리적인 파일은 동등한 관계로 작성됨
- 앱 생성 순서
  - 앱 생성
    - python manage.py staryapp articles (앱의 이름은 복수형 지정 권장.)
  - 앱 등록
    - settings.py INSTALLED APPS안에 articles 넣기

- 프로젝트 구조
  - settings.py 프로젝트의 모든 설정을 관리
  - url.py 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

- 앱 구조
  - admin.py: 관리자용 페이지 설정
  - model. py DB와 관련된 Model을 정의 M
  - views.py 요청처리, 응답반환 V

## 요청과 응답
- 요청 -> url.py  -> views.py (<-> models.py or templates) -> 응답
path('index/', 호출할 view 함수) app쪽에 있는 view함수 가져와야됨
-> from articles import views
path('index/', views.index), 콤마 써라,함수 이름까지만 적어라, 더 적으면 () 호출됨 

def index(request):
  return render(request, 'index.html'(템플릿 경로_templates 이후의 경로))

articles 앱 폴더 안에 templates 폴더 생성
templates 폴더 안에 articles 폴더 생성
articles 폴더 안에 템플릿 파일 생성

