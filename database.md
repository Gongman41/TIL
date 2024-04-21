## database
- 데이터 저장방식
  - 파일로: 쉽게 사용 , 구조적 관리는 어려움
  - 스프레드 시트: 열과 행을 사용해 데이터를 구조적으로 관리 가능
    - 한계: 크기(100만행까지만),보안(제한적인 접근 권한), 정확성
- 데이터 베이스 역할: 데이터 관리,조작
- 관계형 데이터 베이스: 데이터간에 관계가 있는 데이터 항목들의 모임
  - 테이블, 행, 열의 정보를 구조화하는 방식
  - 서로 관련된 데이터 포인터를 저장하고 이에대한 액세스를 제공
  - 데이터를 다양한 방식으로 조회 가능
  - 각 데이터에 고유한 식별값,각 레코드의 고유한 값_ 기본키 부여
  - 다른 테이블의 key값 부여,관계만들기_ 외래키
  - table:데이터를 기록하는 곳
  - field: 각 필드에는 고유한 데이터형식이 지정됨
  - record: 데이터 값
- DBMS: 데이터베이스를 관리하는 소프트웨어 프로그램
  - 데이터 저장 및 관리를 용이하게하는 시스템
  - 데이터베이스와 사용자 간의 인터페이스 역할
  - 데이터 구성, 업데이터, 모니터링, 백업등에 도움
- RDBMS:관계형 데이터베이스를 관리하는 소프트웨어 프로그램

## SQL
- 데이터 베이스에 정보를 저장하고 처리하기위한 프로그래밍 언어
- 테이블의 형태로 구조화된 관계형데이터베이스에게 요청을 질의
  - SQL키워드는 대소문자 구분x 대문자 작성 권장
  - 세미컬런 필요
- SQL Statement: SQL을 구성하는 가장 기본적인 코드블럭
  - DDL: 데이터 정의 CREATE,DROP,ALTER
  - DQL: 데이터 검색 SELECT
  - DML: 데이터 조작 INSERT,UPDATE,DELETE
  - DCL: 데이터 및 작업에 대한 사용자 권한 제어 COMMIT,ROLLBACK,GRANT,REVOKE
- SELECT 선택하려는 필드 FROM 데이터를 선택하려는 테이블
- ORDER by:FROM 뒤에 위치. 오름차순 기본값. ASC|DESC 로 내림차순 정렬
  - 먼저 정렬하고 다음꺼 정렬하면 정렬된 값 안에서 정렬
  - NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력

## Filtering data


# Many to one relationship
## - ex) comment - Article
```py
class Comment(models.Model):
  article = models.ForeignKey(Article,on_delete = models.CASCADE)
```
  - migration 이후 참조하는 대상 클래스 이름 + _ + 클래스이름
  - shell_plus로 데이터 작성시 Article create 이후 comment = Comment()로 인스ㅡ턴스 생성, 변수저장, article = Article.objects.get(pk=1), comment.article = article, 데이터 저장
- 외래키로 참조 테이블 접근 가능
- 역참조: article.comment_set.all(), article.comment_set.get(pk=1)
  - comment_set 이 related manager
  - comments = article.comment_set.all() 같은 식으로 사용
- N:1관계에서 외래키는 N쪽에 작성
- 보통 댓글은 수정할 때 페이지를 따로 이동하지 않기때문에 일단 보류
- 댓글 구현
  - 사용자 댓글데이터 입력받기 위한 form 정의, 해당 페이지에서 랜더링, 외래키는 입력x ,url,view함수에서 처리
```py
class CommentForm(forms.ModelsForm):
  class Meta:
    model = Comment
    # fields = '__all__'
    fields = ('content',)
```
  - url에서 넘겨받은 pk값을 comments_create에 같이 보냄
```py
  def comments_create(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      # 외래키 저장을 위해 변수 저장
      comment.article = article
      comment.save()
      return redirect('articles:detail',article.pk)
    context = {
      'article': article,
      'comment_form':comment_form,
    }
    return render(request,'articles/detail.html',context)
```
  - 댓글 READ는 article 역참조로 해서 context에 같이 보냄
  - delete는 url 따로 작성
    - path('<int:article_pk>/comments/<int:comment_pk>/delete/',views.comments_delete,name='comments_delete')
    - 페이지에서 게시물, 댓글 pk 같이 보냄
```py
def comments_delete(request,article_pk,comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  # article_pk는 redirect를 위해서, article:detail 같이 작성하는 거는 redirect용인듯
  return redirect('article:detail',article_pk)
```
- admim site 등록은 admin.site.register(Article) 이런식
- 댓글이 없는 경우 대체콘텐츠는 {% empty %}{% endfor %} 활용
- 댓글 개수 출력 {{comments|length}} {{ article.comment_set.all|legnth}} {{article.comment_set.count3}}

## - ex) Article - User
```py
from django.conf import settings
class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  pass
```
- User 모델 참조법(User모델은 직접 참조하지않음)
  - get_user_model()_반환값: 객체, models.py 가 아닌 다른 모든 위치
  - settings.AUTH_USER_MODEL_반환값: 문자열, models.py
```py
class ArticleFOrm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ('title','content',)
    # User 외래키 추가떄문
```
```py
@login_required
def create(request):
  if request.method =='POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save(commit=False)
      article.user = request.user
      articel.save()
      return redirect('article:detail',article.pk)
    else:
      pass
```
- 페이지에서 article.user 같이 출력. 외래키로 넣어서 그런듯
- 게시물 update
```py
@login_required
def update(request,pk):
  article = Article.objects.get(pk=pk)
  if request.user == article.user:
    if request.method == 'POST':
      form = ArticleForm(request.POST,instance=article)
      if form.is_valid():
        form.save()
        return redirect('article:detail',article.pk)
    else:
      form = ArticleForm(instance =article)
  else:
    return redirect('article:index')
```
- delete는 메인페이지로 돌아가서 게시물 pk만 받아오는 거랑 요청자랑 작성자 같은지 비교하는 것만 수정
- comment - user 도 같은지 확인하는 거랑 view에서 외래키 넣어주는 것만 추가=    

# many to many rel
- 양쪽 모두에서 N:1 관계를 가짐
- 어느 한 쪽에도 종속되지 않음
- 중개모델에 양쪽 외래키 저장
- django에서는 ManyTomanyField로 중개모델 자동생성
  - 둘중 아무대나 작성 가능. 참조 역참조 관계만 기억
```py
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor)
  name = models.TextField()
```
- 중개모델에 추가정보 필요 시 model 따로 작성 후 through
```py
class Patient(models.Model):
  doctors = models.ManyToManyField(Doctor,though = 'Reservation')
  name = models.TextField()

class Reservation(models.Model):
  doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
  patient = models.ForeignKey(Patient,on_delete = models.CASCADE)
  symptom = models.textField()
```
- patient.doctors.add(doctor1,through_defaults={'sympthom':'flu'}) 예약생성법.
- related_name으로 역참조 manager_name 변경
- symmetrical = True 참조하면 저쪽도 참조(대칭)

## Article - User 좋아요
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
- url 작성하고
```py
@login_required
def likes(request, article_pk):
  article = Article.objects.get(pk = article_pk)
  if request.user in article.like_users.all():
    article.like_users.remove(request.user)
  else:
    article.like_users.add(request.user)
    # add,remove 중개모델 전용
  return redirect('article:index')
