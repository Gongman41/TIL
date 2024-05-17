관-통
클라이언트 서버에 데이터 요청
-  웹 브라우저를 켜서 주소창에 URL을 입력
-  서버에 정보를 요청하는 파이썬 코드 작성

- 라이브러리 사용. 데이터 가져오는 라이브러리: requests
- 파이썬 패키지관리:pip
  - 설치 pip install
  - 목록확인 pip list
- 함수 사용 시
  1. 내 파일 검색
  2. 내장 모듈 모아둔 곳 검색
- 이런 이유로  import 추가
- Not found module 
  - pip list 로 설치 확인
- 현재 파이썬 버전으로 코드 해석
- get()_데이터 가져오기,json()_데이터를 활용하기 좋게 변환
- json() 사용안하면 <Response 200> 이런식으로 옴
  - JSON 형태로 변환. 파이썬의 딕셔너리와 비슷. 객체 표기법
  - 경량 데이터 기반의 데이터 형식. 통신방법, 문법x. 단순히 데이터를 표현하는 방법 중 하나
  - 특징
    - 데이터는 중괄호로 둘러싸인 키-값 ㅆㅇ의 집합으로 표현됨
    - 키 = 문자열 / 값 = 다양한 데이터 유형을 가질 수 있다
    - 값은 쉼표로 구분됨
- API: 클라이언트가 원하는 기능을 수행하기 위해 서버 측에 만들어 놓은 프로그램
  - 서버측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 api를 미리 만들어 둠.
  - 클라이언트는 서버가 미리 만들어 놓은 주소로 요청을 보냄.
  - 보안, 서버할당량 문제로 API 키 발급 후 데이터 요청할 때마다 같이 보냄, 사용량도 정해져 있음_사용량 **제한을 확인해야됨**
  - 파싱: 데이터를 의미있는 구조로 분석하고 해석하는 과정
  - json.loads():JSON형식의 문자열을 파싱하여 딕셔너리로 변경
  - 추가공부 과제
    - data[' '] <-> data.get('weather')



- 파일분리, 포함되는 파일 '_ㅇㅁ눰ㅁㅇ.html' 
- __init__ 모듈로 인식하도록
- runserver 는 개발서버를 실행
- 배포용(deploy)_클라우드 서비스_리눅스_네트워크
  - pythonAnywhere
  - asgi
  - wsgi
- settings.py/DATABASES 에서 데이터베이스 지정.
- URI에는 데이터 위치
- 행동은 http method
- API server_데이터 조작만 <-> return render 화면
- django에서 실제 DB 요청은 데이터를 실제로 사용을 할때(템플릿)
  - 지연로딩.ORM 사용 시. 실제 데이터가 필요할 떄 가져오기. 중복된 sql문 방지 + 효율적 관리
  - N + 1 problem
  - 해결_ 즉시로딩: annotate ,select_related(정참조시에 발생하는 중복쿼리 해결), prefetch_related(역참조시에 발생하는 중복쿼리 해결)
- get_object_or_404: 에러 발생하지 않고 404페이지
- ModelForm(정의해놓은 필드만 입력받고 싶어)_ModelSerailizer <-> Form(내가 원하는 필드가 추가로 있어)_Serailizer
- FK 입력 x
  - 사용자가 사용할 떄 이상함
  - 다른 테이블의 데이터를 참조. 입력 받을 시 없는 데이터 받을 수도
- django seed_ 테스트데이터 만들어주는 라이브러리
  - psycopg2 도 설치
  - settings.py에 넣어주고
- django-debug-toolbar





settings에 rest_framework
render, redirect는 페이지 자체를 return
jsonResponse(django.http),Response(rest_framework.response).
settings에서 API_KEY 사용법
전체 프로젝트 디렉토리에 .env 생성. 거기에 API_KEY 변수 작성. .gitignore에 .env 넣어주기.
settings.py 에 import os , import environ
```py
import os
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
  env_file=os.path.join(BASE_DIR,',env')
)
WEATHER_API_KEY = env('API_LEY')
```
다른 곳에서 from django.conf import settings 하고 
api_key = settings.WEATHER_API_KEY 로 받아서 사용


seializers.py

```py
from rest_framework import serializers
from .model import weather
# serializers.ModelSerializer 모델필드에 정의된 애들만 변환
# serializers.Serializer 없어도 추가로 변환
class WeatherSerialize(serializers.ModelSerializer)
  class Meta:
    model = Weather
    fields = '__all__'
```
views.py
```py
from .serializers import WeatherSerializer
# ...
save_data = {
  # ...
  pass
}
serializer = WeatherSerializer(data = save_data)

# 유효성 검증, 유효 시 저장, many=True
if serializer.is_valid(raise_exception=True)
  serializer.save()
return JsonResponse({'message':"save okay!"})
```
@api_view(["GET"])
from rest_framework.decorators import api_view
- api함수 구현 시 붙여줘야됨. 
- JsonResponse 는 장고꺼라 버그 안나옴
- Response 일때는 필수/.

```py
weathers = Weather.objects.filter(temp__gt=(20 + 273.15))
serializer = WeatherSerializer(weathers,many = True)
return Response(serializers.data)

```

## Locust

##

index.js, views 작성
stores 작성. 외부에서 데이터 가져오는 함수 작성(axios_then,catch)
``` js
const getProducts = function() {
  axios({
    method:'get',
    url: 'asdsad'
  })
  .then((response)=>{
    // console.log(response)
    products.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
}
// goRoute : 받을떄
//  useRouter: 보낼 떄
const router = useRouter()
const goDetailPage = function(productId) {
  router.push(`/${productId}`)
}

const carts = ref({})

const addCart = function(product) {
  carts.value.push(product)
}
const deleteCart = function() {
  const idx = carts.value.findIndex(cart => cart.id ===productId)
  if (idx !== -1) {
    carts.value.splice(idx,1)
  }
}
```
```js
const route = useRoute()
const productId = route.params.product_id
// store에서 가져오면 바로 디테일페이지로 접근 시 데이터가 없음
// api가 제공해주면 ㅇㅋ, 아니면 app.vue등 상위 컴포넌트에서 호출_대신 데이터가 있다면 재호출 하지 않도록 구현
// 여기서만 쓰니까 여기다 함수 작성
const product = ref({})
 axios({
    method:'get',
    url: `asdsad${productId}`
  })
  .then((response)=>{
    // console.log(response)
    products.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })

  
```
template script에서 onmounted(비동기 요청

콘텐츠 기반 필터링
협력 필터링(최근접 이웃 기반,잠재요인 기반)
하이브리드 추천 시스템
http://www.storyjoa.com/monster/bbs/board.php?bo_table=AIcon&wr_id=23
https://www.kaggle.com/code/alsojmc/movie-recommender-systems
https://velog.io/@skarb4788/%EB%94%A5%EB%9F%AC%EB%8B%9D-%EC%98%81%ED%99%94-%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C
https://web.archive.org/web/20180426032401id_/http://kiise.or.kr/e_journal/2012/4/SA/pdf/02.pdf
https://velog.io/@kim_haesol/%EC%98%81%ED%99%94-%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C
https://diane-space.tistory.com/90
https://github.com/yuna872/Movie-Spotter
https://m.blog.naver.com/jaehong7719/221905709680
https://heegyukim.medium.com/%EC%B6%94%EC%B2%9C-%EC%8B%9C%EC%8A%A4%ED%85%9C-1-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%EC%BD%98%ED%85%90%EC%B8%A0-%EA%B8%B0%EB%B0%98-%EC%B6%94%EC%B2%9C-a52fbca5722a
https://continuous-development.tistory.com/141
https://lsjsj92.tistory.com/570
https://anweh.tistory.com/41
https://m.blog.naver.com/mmwook94/221388978684
https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0015074637
콘텐츠 기반 필터링: 항목의 내적 특징기반 유사성 측정

  취향 변화 반영 어렵


아이템 기반 협력 필터링: 사용자의 행동 데이터 기반 유사성 측정
  취향 변화에 잘 대응
    - 콜드 스타트: 새로운 유저나 새로운 아이템이 추가되었을 때 유사도 계산 데이터 부족
    - 계산량: 사용자, 유저 추가 시 계산량 많이 증가
    - 롱테일: 소수의 인기항목에만 관심, 비인기 항목에는 추천정보 부족
잠재모델 기반:


장고 view에 작성 후 받아오기