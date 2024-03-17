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
  - pip freeze >(문자열을 쓰겠다)requirements(다른이름 가능하긴 한데 그냥 이렇게 고정).txt
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
    - python manage.py startapp articles (앱의 이름은 복수형 지정 권장.)
  - 앱 등록
    - settings.py INSTALLED APPS안에 articles 넣기

- 프로젝트 구조
  - settings.py 프로젝트의 모든 설정을 관리
  - url.py 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

- 앱 구조
  - admin.py: 관리자용 페이지 설정
  - model.py DB와 관련된 Model을 정의 M
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

pip install -r requirements.txt

- render 함수: 템플릿에서 사용할 데이터 context는 딕셔너리 타입으로 작성
- 데이터를 받아서 보내고 싶다. urls.py 에 적고 render에 매개변수로 받고 보냄. 근데 이걸 url로 받는게 아니라 input으로 받아서 넘기거나 서버에서 가져오는 게 보통이잖아. 그걸 뒤에서
# Tempolate, URLS
## Template system
- 데이터 표현을 제어하면서 표현과 관련된 부분을 담당
- HTML의 콘텐츠를 변수 값에 따라 바꾸고 싶으면 views.py에서 context로 변경
- DTL: template에서 조건,반복,변수등의 프로그래밍적 기능을 제공하는 시스템
  - variable: render함수의 세번째 인자로 딕셔너리 데이터를 사용. key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨. . 을 사용하여 변수 속성에 접근할 수 있음
  - Filters: 표시할 변수를 수정할 때 사용(변수+|+변수). 연결이 가능하며 일부 필터는 인자를 받기도 함.
  - Tags: 반복 또는 논리를 수행하여 제어 흐름을 만듦. 일부 태그는 시작과 종료 태그가 필요
  - comments: {# dsds #}, {%comment%} ... {%endcomment%}

django document 검색어  로 구글에 검색
대제목보고 목차보기

## 템플릿 상속
- 만약 모든 템플릿에 bootstrap을 적용하려면_모든 템플릿에 bootstrap CDN을 작성해야?
- 페이지의 공통요소를 포함하고 하위 템플릿이 재정의할 수 있는 공간을 정의하는. 기본skleton 템플릿을 작성하여 상속구조를 규정
- extends tag: 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림. 2개이상 사용 불가. 자식 템플릿 최상단에 작성
- block tag: 하위 템플릿에서 재정의 할 수 있는 블록을 정의(상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간을 마련.) 여러 개가 작성되기 때문에 이름 필요

## HTML form
- 데이터를 보내고 가져오기
- HTML form element를 통해 사용자와 애플리케이션간의 상호작용 이해하기
- URL에 주소 입력해서 요청, HTML form 태그로
- form element: 사용자로부터 할당된 데이터를 서버로 전송, 웹에서 사용자 정보를 입력하는 여러 방식(text, password,checkbox 등)을 제공


- action:어디, 입력데이터가 전송될 URL을 지정. 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐
- method:방식. GET(URL노출), POST(로그인. URL에 데이터 노출x, 인증 때 다시)
- input(type 속성값에 따라 다양하게 받음))
- name: 입력한 데이터에 붙이는 이름
- input의 name속성의 key를 보내줘서 데이터를 처리. 데이터를 제출했을 떄 서버는 name속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근
input의 결과는 결국 주소의 변경
- 여러 개의 데이터는 & 로 연결된 key=value쌍으로 구성, 기본 URL과는 ?로 구분됨
- request에는 form으로 전송한 데이터뿐만 아니라 모든 요청관련 데이터가 담겨있다
- request.GET 은 딕셔너리값을 가져오고 .get('message')로 value 값 가져옴
- tempate 위치 지정. BASE_DIR은 최상단 폴더. 이렇게 작성하는 거는 운영체재별로 자동 변환을 위해
- urls _ 분배기.많은 부분이 중복되고 url의 일부만 변경되는 상황 <type:변수이름>

## URLS
- App Url mapping: 각 앱에 urls.py 생성
- project의 url에서는 어느 앱으로 보낼지만 결정.
- variable routing: URL일부에 변수를 포함시키는 것. 템플릿에 많은 부분 중복, URL의 일부만 변경되는 상황일 때 사용
  - <path_converter:variable_name>
  - path_converter: URL변수의 타입을 지정
- include: 프로젝트 내부 앱들의 URL을 참조할ㅇ 수 있도록 매핑하는 함수. URL의 일치하는 부분까지 잘라내고 남은 문자열부분은 후속처리를 위해 include된 URL로 전달ㅇ
- url 구조 변경에 따른 문제점: 해당 주소 사용하는 모든 위치 가서 고쳐야됨(템플릿들) -> 이름을 따로 지어줌 + 앱이름을 앞에 태그로 사용
-  url tag: 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
- app_name 변수값 설정
- variale 라우팅에서 html에서 받을 때 변수1 변수2 같이 받음
## Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공_ 테이블 구조를 설계하는 청사진
```py
#articles/models.py
class Article(models.Model)
  title = models.CharField(max_length=10)
  content = models.TextField()
```
- id필드는 django가 자동 생성. 작성한 모델 클래스는 DB에 테이블구조만듦
- 열 = 필드
- Model이라는 부모 클래스를 상속받음. model 관련 모든 코드가 작성되어있음. 테이블 구조 설계할 코드만 작성하면 됨
- 필드(열)이름, 필드 데이터 타입, (선택)필드 제약조건.
- migrations model 클래스의 변경사항을 DB에 최종 반영하는 방법,최종 설계도. model클래스는 설계도 초안
makemigrations(최종설계도, git commit 유사), migrate(최종설계도 DB에 전달하여 반영, push)

- 이미 생성된 테이블에 필드를 추가해야 한다면 기본값 설정이 필요_ 현재 대화를 유지하면서 직접 기본값 입력. 빈 값, 빈 필드 추가 불가
```py
#articles/models.py
class Article(models.Model)
  title = models.CharField(max_length=10)
  content = models.TextField()
  created_at = models.DataTimeField(auto_now_add = True)
  #데이터가 처음 생성될때만 자동으로 현재 날짜시간을 저장
  updated_at models.DataTimeField(auto_now=True)
  #데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
```
- Model field: 데이터타입과 제약조건 정의, 필드 정의
-  charField: max_length 는 필수 인자. 필드의 최대길이 결정
- TextField() 글자수가 많을 때 사용
- admin 계정생성 : python manange.py createsuperuser
- admin.py에 작성한 모델 클래스 등록
  - from .models import Articles
  - admin.site.register(Article)
- 데이터베이스 초기화: migration 파일 삭제(폴더x), db.sqlite3 파일 삭제.


## 반응형 웹사이트 구현
1. 어떤 내용이 들어갈지
2. 그 내용을 어디다가 표시할지
3. 반응형 디자인 ->에 따라서 내용을 어디에 표시할지

1. 라이브러리나 프레임워크
2. 시맨틱 태그_의미가 있는 태그, 검색엔진 최적화, 가독성, 유지보수_를 사용할 지 대략적인 그림