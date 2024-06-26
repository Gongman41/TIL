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

# ORM
- admin에서 진행했었음
- ORM: 객체지향 프로그래밍 언어를 사용하여 호환되지않는 유형의 시스템간에 데이터를 변환하는 기술._서로 다른 언어
- querySet api: ORM에서 데이터를 검색,필터링,정렬 및 그룹화 하는 데 사용하는 도구
  - API를 사용하여 SQL이 아닌 Python코드로 데이터 처리
  - Article_(model class).objects(manager_는 안바뀜).all()(queryset api)
  - query set: 데이터 베이스에게서 전달받은 객체목록, 순회 가능. Django ORM을 통해
    - 만들어진 자료형. 단일한 객체 반환 시 모델 인스턴스로 반환
  - 모델클래스와 인스턴스를 이용해 DB에 데이터 저장,조회,수정,삭제하는 것.
  - Django shell; Django 환경 안에서ㅕ 실행되는 python shell.
  
## CRUD

- 데이터 객체를 만드는 3가지 방법
    - 인스턴스 변수를 추가
    - save() 메서드(그 전 migrate)
  - 
  - id <-> pk
- 조회 메서드
  - all()
  - filter()
  - get(): 찾을 수 없거나 둘 이상의 객체를 찾으면 예외 발생. 고유성을 보장하는 조회에서 사용_pk
- 수정
  - 조회 후 값 재설정
- 삭제
  - 조회 후 delete 메서드 호출
  - 삭제한 id값 재사용하지 않음

## field lookups
- 특정한 레코드에 대한 조건을 설정하는 방법
- 디테일한 조건

QuerySetApi
MakingQueries

## ORM with View
- 전체게시글 조화
- create 로직을 구현하기위해 필요한 view함수의 개수는? 2개
  - throw, catch _ new, create

## HTTP request method
- 데이터에 어떤 요청을 원하는지를 나타내는 것
- GET:특정 리소스를 조회하는 요청. URL에 넣어서 보내짐
- POST:특정 리소스에 변경을 요구하는 요청(DB에 직접적인 변화). HTTP body에 담겨 보내짐
- HTTP response status code ex) 404, 403
  - CSRF: 사이트 간 요청 위조. 자신의 의지와 무관하게 공격
  - CSRF Token 내가 만든 페이지라는 인증서 같은 토큰
  - DB에 조작을 가하는 요청이기 때문에 POST는 Token확인
  - post 요청은 redirect_어딘가로 보내버림 == 사용자가 GET요청을 한번 더 보내도록 해야한다

Delete
Update 함수 2개

## HTML 'form'
- 유효한 데이터인지 확인 필요.
  - 유효성 검사
- django Form: 사용자 입력데이터를 수집하고 처리 및 유효성 검사를 수행하기 위한 도구.
  - 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
  - forms는 css만 대체, 유효성은 create쪽에서

- widget: input의 표현을 바꿈

- django ModelForm: 사용자 입력데이터를 db에 저장해야 할때.
<-> Form:저장하지 않을때_로그인<->회원가입

new, create view: 생성 담당, (new)GET-(create)POST 차이

## Static files
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일(이미지,js,css파일)
- 웹서버의 기본동작: 특정 위치(URL)에 있는 자원을 요청, 응답
  - 정적파일도 제공을 위해서는 경로(URL)가 필요
- static file 제공하기
  - templates랑 비슷
  - 기본경로: 장고가 약속한 경로.
    - STATILC_URL: 기본 경로 및 추가 경로를 참조하기 위한 URL
      - URL + STATIC_URL + 정적파일 경로
  - 추가경로: STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
- load는 extends 아래. load는 상속 안됨.

## Media Files
- ImageField(): 이미지 업로드에 사용하는 모델필드_ 부모가 캐릭터 필드
  - 이미지 객체가 직접 저장되는 것이 아닌 이미지파일의 경로가 문자열로 DB에 저장
  - settings.py에 MEDIA_ROOT,MEDIA_URL 설정
  - 세팅한 MEDIA_ROOT(실제 미디어 파일들이 위치하는 디렉토리의 절대경로),MEDIA_URL(STATIC_URL과 동일한 역할)에 URL 지정
  - form쪽에 enctype 설정 필요, view함수도 FILES
  - 파일 경로만 저장

- 업로드 이미지 제공
  - 같은 이름의 파일 업로드 시 랜덤 문자열 추가해주ㅠㅁ
- 업로드 이미지 수정
  - 수정해도 파일 삭제 x. 필요하면 라이브러리 사용

# 인증시스템
## Cookie & Session
- 서버로부터 페이지를 받았을 때 계속 연결되어있는 상태 x
- HTTP
  - 비연결지향: 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 무상태: 상태라는 게 없음_로그인 상태 유지 불가, 장바구니 상품 유지 불가
- 쿠키: 서버가 사용자 웹브라우저에 전송하는 작은 데이터 조각. 웹페이지랑 같이 줌
  - 사용자 인증, 추적, 상태유지등에 사용되는 데이터 저장 방법
  - 같은 서버에 다른 페이지로 재 요청마다 저장해놨던 쿠키를 함께 전송
  - 브라우저는 쿠키를 Key-Value 데이터 형식으로 저장
  - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때, 상태 판단 시 주로 사용.
  - 세션관리, 개인화, 트래킹 (시크릿모드는 개인화,트래킹 방지)
    - 세션: 서버 측에서 생성되어 클라이언트와 서버간의 상태를 유지. 상태정보를 저장하는 데이터 저장방식
  - 작동 원리
    - 클라이언트가 로그인을 하면 서버가 session 데이터 생성 후 저장(기한 설정 가능)
    - session id 발급
    - 발급한 session id를 클라이언트에게 응답
    - 클라이언트는 응답받은 session id를 쿠키에 저장
    - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함꼐 쿠키를 전달
    - 쿠키는 요청할 때마다 서버에 함꼐 전송. 서버에서 session id를 확인해 로그인 되어있다는 것을 알도록 함.
  - 수명
    - session cookie:현재 세션이 종료되면 삭제, 브라우저 종료와 함께 삭제
    - persistent cookies: Expires 속성에 지정된 날짜 혹은 Max-Age속성에 지정된 기간이 지나면삭제
  - django는 database-backed sessions 저장방식이 기본값.
    - session정보는 DB의 django_session 테이블에 저장 
    - admin
## Authentication
- 사용자가 누구인지 확인하는 것

## Custom User model
- admin
- user model 대체하기
  - 개발자기 직접 수정할 수 없는 문제
  - 기존의 userclass와 동일한 class를 이름만 바꿔서

## Login & Logout
- Login: Session을 Create하는 과정
- AuthenticationForm():로그인 인증에 사용할 데이터를 입력받는 빌트인 form(DB 저장 x) <-> model-form(DB에 저장)
- Logout: Session을 Delete하는 과정
  - 현재 요청에 대한 Session data를 db에서 삭제. 클라이언트의 쿠키에서도 Session id를 삭제
- abstact base classes
  - 몇 가지 공통정보를 여러 다른 모델에 넣을 떄 사용하는 클래스
  - 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가돔;

## 회원 가입
- User 객체를 create하는 과정
  - UserCreationForm: built-in ModelForm(DB에 저장). 회원 가입 시 사용자 입력데이터를 받음.

## 비번 변경
- 인증된 사용자의 Session 데이터를 Update 하는 과정
- PasswordChangeForm(): built-in form

## 로그인 사용자 접근 제한
-  is_authenticated 속성
-  login_required 데코레이터
