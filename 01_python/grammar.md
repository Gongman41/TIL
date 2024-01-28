# 파이썬_문법
## 프로그램이란
- 프로그램: 명령어들의 집합
  - 프로그램은 기초 연산으로 구성
  - 컴퓨터에 여러 연산집합 생성가능
  - 핵심: 새 연산을 정의하고 조합해 유용한 작업을 수행하는 것 -> 문제를 해결
## 프로그래밍 언어
-  프로그래밍 언어: 컴퓨터에게 작업을 지시하고 문제를 해결하는 도구\
-  파이썬
   -  간결하고 읽기 쉬운 문법
   -  다양한 응용분야(데이터 분석, 인공지능, 웹 개발, 자동화 등)
   -  파이썬 커뮤니티의 지원(온라인 포럼, 커뮤니티 생태계)
   -  실행 방법: 컴퓨터는 기계어로 소통하기때문에 기계어를 직접 작성하기 어려움
      -  인터프리터가 사용자의 명령어를 기계어로 번역시켜줌(훨씬 사용하기 쉽고 운영체제간 이식도 가능_확장성)
      -  shell_한번에 한 명령어씩(python -i), 확장자가 .py인 파일에 작성된 파이썬 프로그램 실행

## 표현식과 값
- 표현식 : 값,변수, 연산자 등을 조합하여 계산되고 결과를 내는 코드 구조
- 평가: 표현식이나 문장을 실행하여 그 결과를 계산하고 값을 결정하는 과정. 표현식이나 문장을 순차적으로 평가하여 프로그램의 동작을 결정
- 문장: 표현식보다 좀 큰 범위. 실행가능한 동작을 기술하는 코드(조건문, 반복문, 함수 정의 등), 문장은 보통 여러 개의 표현식을 포함.

## 타입
-  타입: 값이 어떤 종류의 데이터인지, 어떨게 해석되고 처리되어야 하는 지를 정의(연산자, 피연산자)
-  데이터 타입_피연산자
   -  숫자형:int, float, complex
   -  시퀀스타입: list, tuple, range
   -  텍스트 시퀀스타입: str
   -  set, dict..
- 산술 연산자: -(음수부호, 뺄셈),*(곱셈),/,//(몫만),%,**(지수)-
- 연산자 우선순위: 산술계산이랑 똑같.

## 변수와 메모리
- 변수: 값을 **참조**하는 이름. 
  - 할당문: degrees = 36.5
    - degres는 값 36.5를 참조.값을 갖는 게 아니라 주소를 값의 주소를 갖는다.
    - 할당 연산자(=): 오른쪽에 있는 표현식을 평가해서 값(메모리주소)을 생성
      - 존재하지 앟는 변수라면 새 변수를 생성
      - 기존에 존재했던 변수라면 기존 변수를 재사용해서 변수에 들어있는 메모리 주소를 변경
      - 변수에 재할당. 위에서부터 평가.
  - 객체: 타입을 갖는 메모리 주소 내 값, 값이 들어있는 상자. 36.5
  - 메모리의 모든 위치에는 그 위치를 고유하게 식별하는 메모리 주소가 존재.
  - 변수명 규칙: 영문 알파벳, 언더스코어, 숫자로 구성, 띄어쓰기 구분, 대소문자 구분, 숫자로 시작불가

## Style guide
- style guide: 코드의 일관성과 가독성을 향상시키기위한 규칙과 권장사항들의 모음(프로그래밍 맞춤법)
  - 변수명, 들여쓰기(공백4칸),줄 길이 79자 제한, 함수 정의 등의 블록사이에는 빈 줄 추가, 문자와 밑줄을 사용해 이름작성
  
  *Python tutor: 알고리즘 풀 때 어떻게 실행되는 지 도와주는 시각화 도우미.

## 주석
- 주석: 프로그램 코드 내에 작성되는 설명이나 메모
- 인터프리터에 의해 실행되지 않음
- """ """(여러줄 주석),#(한줄 주석)_활성화 비활성화 편함,ctrl / ->주석 활성화, 비활성화.
- 코드의 특정 부분을 설명하거나 임시로 코드를 비활성화 할 때

## Data Types
- data types: 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
- 필요성: 값들을 구분, 다루는 법 알 수 있음. 오류 예방

### Numeric types
- int: 정수 자료형
  - 2진수(0b),8진수(0o), 16진수(0x)
- float: 실수 자료형_실수에 대한 근삿값
  - 유한 정밀도: 메모리 용량 한정, 한 숫자에 대해 저장하는 용량 제한_2/3,5/3에 가장 가까운 값
  - 실수 연산 시 주의사항
    - 컴퓨터는 2진수, 사람은 10진수. 
    - 0.1을 컴퓨터로 표현하면 무한대로 반복 -> 근삿값으로 표현
    - 이를 floating point rounding error(부동소수점 오류)
    - math  모듈 활용, 임의의 작은수 활용
- 지수 표현 방식
  - e 또는 E를 사용한 지수 표현

### Sequence Types
- 여러 개의 값들을 **순서**대로 나열하여 저장하는 자료형
- 특징
  - 순서대로 저장(<->정렬)
  - 인덱싱: 각 값에 고유한 인덱스를 가지고 있으며 인덱스를 사용하여 특정위치의 값을 선택하거나 수정
  - 슬라이싱: 인덱스 범위를 조절해 부분적인 값을 추출가능
  - 길이: len() 함수를 사용하여 저장된 값의 개수(길이)를 구할 수 있음
  - 반복: 반복문을 사용하여 저장된 값들을 반복적으로 처리할 수 있음
- **str**: 문자들의 순서가 있는 변경 불가능한 시퀀스 자료형
  - 문자열 표현: 문자열은 '', ""로 표현. 하나로만 작성.
  - 문자열은 불변. 값이 메모리가 들어가있음. 바꾸고 싶으면 재할당을 해야됨.
  - 중첩 따옴표: 따옴표 안에 따옴표 작성 시 다른 따옴표로 작성.
  - strint interpolation: 문자열 내에 표현식이나 변수를 삽입하는 방법
    - f-string: 문자열에 f또는 F접두어를 붙이고 표현식을 {}로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있음.
- 인덱스: 시퀀스 내의 값들에 대한 고유한 번호로 각 값의 위치를 식별하는 데 사용되는 숫자_ 음수 인덱스도 제공
- 슬라이싱: 시퀀스의 일부분을 선택하여 추출하는 작업.새로운 시퀀스를 생성. 미작성된 부분은 그대로 끝까지.
  - ``my_str[0:5:2]`` 0-5까지 2칸씩.
  - **``mt_str[::-1]`` 문자열 뒤집기**

*Escape sequence
  - 역슬래시 뒤에 특정 문자가 와서 특수한 기능.\n, \t, \\, \', \"
 len() : 리스트 길이 출력
 인덱스,키로 값 호출 시 []로
 온라인 독서실 사운드 탐지 후 강퇴 시스템
 ctrl shift p
- **list**: 여러 개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형
  - 대괄호로 표기
  - 데이터는 어떤 자료형도 저장 가능
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 가변
  - 없는 인덱스 직접 출력 시 오류. 범위내면 오류 x
  - 할 수는 있지만 예외처리가 되지않아 예상치 못한 상황이 발생할 수 있다
- **tuple**
  - 소괄호로 표기
  - 데이터는 어떤 자료형도 저장 가능
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 불변
  - 안전하게 여러 값을 전달, 그룹화, 다중할당 등
  - 파이썬 내부 동작에서 주로 사용됨
  - a = (1,) 빈공간을 넣지 않으면 그냥 정수 1이 되버림. 요소 1개를 가진 튜플임을 보여주려면 저ㄹ렇게 빈 공간 표시
  - 여러 변수 한꺼번에 변수 할당 가능.(튜플로 취금, 괄호 생략도 가능)
  - 슬라이싱해도 튜플
- **range**
  - 연속된 정수 시퀀스를 **생성**하는 변경불가능한 자료형
  - range(n,m): n부터 m-1까지의 숫자 시퀀스
  - 아직 포장이 안풀린 느낌.
  - 타입을 바꿔서 사용하거나(list()) 반복문에서 사용

### Non-sequence Types
- **dict**: key - value 쌍으로 이루어진 순서와 중복이 없는 변경가능한 자료형_중복 시(뒤에 다시 선언시) 뒤에 선언된 값으로 수정
  - key는 변경 불가능한 자료형만 사용가능(int,str,float,tuple,range...)
  - value는 모든 자료형 사용 가능
  - 중괄호로 표기
- **set**: 순서와 중복이 없는 변경 가능한 자료형
  - 수학에서의 집합과 동일한 연산처리 가능
  - 중괄호로 표기
  - |(합집합),-(차집합),&(교집합)
  - 빈 set만들 때 {}x set()로 만들어야됨

### Other Types
- **None**: 파이썬에서 '값이 없음'을 표현하는 자료형
- **Boolan**: 참과 거짓을 표현하는 자료형
  - 비교/ 논리 연산의 평가 결과로 사용
  - 주로 조건/ 반복문과 함께 사용
- **collection**: 여러 개의 항목 또는 요소를 담는 자료 구조. 변경가능 여부(주소 변경 가능 여부), 순서 여부.

### Type Conversion
- 암시적 형변환: 파이썬이 자동으로 형변환을 하는 것_Boolean과 Numeric Type에서만 가능
  - int + float -> float
- 명시적 형변환: 개발자가 직접 형병환을 하는 것
  - str -> interger: 형식에 맞는 숫자만 가능
  - integer -> str: 모두 가능
  - range,dict제외 다 가능(key만)
## 연산자
- 산술연산자: -,+,*,/,//,%,**
- 복합 연산자: +=,-=,*=,/=,//=,%=,**=
- 비교 연산자: <,<=,>,>=,==,!=,is(같음),is not(같지않음)
  - is 비교 연산자: ==는 동등성_주소 비교, is는 식별성_값을 비교(None,True,False등을 비교할 때 사용,타입자체가 주소가 정해져 있음.)
  - 메모리 내에서 같은 객체를 참조하는지 확인
- 논리 연산자: and, or, not(단일 피연산자를 부정), 비교연산자와 함께 사용가능
  - 단축평가: 논리 연산에서 두번째 피연산자를 평가하지 않고 결과를 결정하는 동작...?
  - and_첫번째  False 시 끝
  - or_첫번째 True시 끝
  - 코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함
- 멤버십 연산자: 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인
  - in: 오른쪽 피연산자의 시퀀스에 속하는 지 여부를 확인
  - not in: 그 반대
- 시퀀스형 연산자: +(결합 연산자),*(반복 연산자)

## 함수
- 함수: 특정 **작업**을 수행하기 위한 **재사용** 가능한 코드 묶음
  - 코드의 중복을 방지
  - 재사용성,가독성, 우지보수성 향상
- 내장 함수(built-in function): 파이썬이 기본적으로 제공하는 함수(import없이 바로 사용 가능_ex.print)
  - 절대값을 만드는 함수 abs
- 함수 호출: funtion_name(arguments). 함수의 이름을 사용하여 해당 함수의 코드 블록을 실행하는 것(소괄호 필수)
- 함수 구조
  - ```python
    def make_sum(pram1,pram2)
    ..
    ..# 함수의 body
      return pram1 + pram2 #반환값
    ``` # """ """: Docstring_함수를 설명하는 가이드 작성
  - pram1,pram2: 파라미터, 매개변수 
  - 함수 정의
    - def 키워드로 시작(define)
    - def 이후 함수 이름 작성
    - 괄호안에 매개변수 정의가능
    - 매개변수는 함수에 전달되는 값을 나타냄
  - 함수 body
    - 콜론 다음에 들여쓰기된 코드 블록
    - 함수가 실행될 떄 수행되는 코드를 정의
    - Docstring은 함수 body앞에 선택적으로
  - 함수 반환 값
    - 결과 반환 가능
    - return 이후 반환할 값 명시
    - 함수 실행 종료, 결과를 호출 부분으로 반환
  - 함수 호출
    - 함수의 이름과 필요한 인자(argument)를 전달해야함
    - **호출** 부분에서 전달된 **인자**는 함수 **정의** 시 작성한 **매개변수**에 대입됨
    - return이 없으면 호출 시 할당 불가. 출력 시 None
### 매개변수와 인자
- 매개변수: 함수를 정의할 때 함수가 받을 값을 나타내는 함수
- 인자: 함수를 호출할 떄 실제로 전달되는 값
  - 인자의 종류
    - 위치인자: 함수 호출 시 인자의 위치에 따라 전달되는 인자(위치인자는 함수 호출 시 반드시 값을 전달해야함)
    - 위치인자는 생략 불가
    - 기본 인자값
      - 함수 정의에서 매개변수에 기본 값으 ㄹ할당하는 것
      - 함수 호출 시 인자를 전달하지않으면 기본값이 매개변수에 할당됨
    - 키워드 인자
      - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자\
      - 매개변수와 인자를 일치시키지 않고 특정매개변수에 값을 할당할 수 있음
      - 인자의 순서는 중요하지 않으며 인자의 이름을 명시하여 전달. 
      - 호출 시 키워드 인자는 위치인자 뒤에 위치해야함
    - 임의의 인자 목록(가변)
      - 정해지지 않은 개수의 인자를 처리하는 인자
      - 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리(print함수)
    - 임의의 키워드 인자 목록(가변 키워드)
      - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
      - 함수 정의 시 매개변수 앞에 '**'를 붙여 사용하며 여러 개의 인자를 dictionary로 묶어 처리
    - 함수 인자 권장 작성순서
      - 위치 -> 기본 -> 가변 -> 가변 키워드
      - 가변은 비워놔도 문제 없
      - 가변과 가변키워드로 만들고 가변키워드만 인자로 넣으면 가변은 빈 튜플로 나옴
  ## 함수와 스코프
  - scope
    - global scope: 코드 어디에서든 참조할 수 있는 공간
    - local scope: 함수가 만든 scope(함수 내부에서만 참조가능), 특정 인덱스의 리스트 값은 변경 가능
  - variable
    - global variable
    - local variable: 함수 내부에서만 값 존재.
  - 변수 수명주기
    - built-in scope:파이썬 실행된 이후부터 영원히 유지
    - global scope: 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
  - 이름 검색 규칙: 파이썬에서 사용되는 이름(식별자)들은 특정한 namespace에 저장되어 있음.
    - LEGB Rule
      - local scope
      - enclosed scope
      - global scope
      - built-in scope
    - 내부에서 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음
    - 현재 scope의 저장된 값 먼저 호출
    - **함수 정의와 호출 구분**
  - global 키워드
    - 변수의 스코프를 전역 범위로 지정하기 위해 사용
    - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용_알고리즘 시 활용
    - global 키워드 선언전에 접근 or 매개변수에 global 사용불가
    - 인자, 반환값으로 함수로 값 변경 권장
    - 로컬에서 나오고 다른 로컬로 들어가면 해제..?
  ## 재귀함수
  - 재귀 함수: 함수 내부에서 자기 자신을 호출하는 함수
    - 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며 코드의 가독성이 높아짐
    - 1개 이상의 base case(종료되는 상황)가 존재하고 수렴하도록 작성
    - 큰 문제를 작은 문제로 줄어들여서 풀 떄 많이 사용
    - ex) 팩토리얼
    - 종료조건을 명확히, 반복되는 호출이 종료 조건을 향하도록
## 유용한 함수
  ### 유용한 내장함수
  - map(function, iterable)
    - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고 그 결과를 map object로 반환
    - 첫번째 위치인자로 함수를 받음. iterable은 반복이 가능한 친구들
    - 함수를 iterable에 하나하나 적용. 마치 반복문
    - map 객체로 저장. list()로 변환 필요
  - zip(*iterables)
    - 임의의 iterables를 모아 튜플을 원소로 하는 zip object를 반환
    - list() 사용 필
    - 개수가 다르다면?
  - lambda 함수: 이름없이 정의 되고 사용되는 익명함수
    - lambda 매개변수: 표현식\
    - 키워드 매개변수(여러개이면 쉼표로 구분) 결과값을 반환하는 표현식으로 작성
    - 간단한 연산이나 함수를 한 줄로 표현할 때 사용.
    - 함수를 매개변수로 전달하는 경우에도 유용하게 활용
  - packing: 여러 개의 값을 하나의 변수에 묶어서 담는 것
    - 변수에 담긴 값들은 튜플형태로 묶임
    - *는 남는 요소들을 리스트로 패킹하여 할당_가변인자 작성가능 이유
  - unpacking: 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
    - 튜플이나 리스트등의 객체의 요소들을 개별 변수에 할당
    - *는 리스트의 요소를 언패킹
    - **는 딕셔너리의 키-값 쌍을 함수의 키워드 인자로 언패킹
    - 매개변수와 키값이 같아야 가능

  - * : 패킹연산자 시 여러 개의 인자를 하나의 튜플로 묶는 역할, 언패킹 시 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
  - **: 언패킹 시에만 딕셔너리-키값 쌍을 키워드 인자로 언패킹하여 함수의 인자로 전달하는 역할

*메서드: 누군가가 가지고 있는 함수 
*내장함수: 파이썬이 기본적으로 가지고 있는 함수
sorted(function), sort(메서드) 리턴이 있냐 없냐
실행과 할당의 차이
- list.sort()메서드는 정렬 대상인 주어(리스트)기 정해져있다. 원본을 정렬
- 반면 sorted 함수는 '누구를' '정렬'할 것인지 정해 줘야한다 -> 인자를 넘긴다. 원본은 변경x 정렬한 결과값만 반환
 점화식 특정 조건이 소진되어 자연스럽게 종료됨

 딕셔너리 언패킹 리스트. 순서 만들어서 확인하기 편하게




 .format()
 sorted가 함수 sort는 메서드. 문자열도 정렬

 def sorted(iterable, key=None, reverse=False):
    pass
sorted(list, reverse=True)  #None 
print('' == False)
print('' == True)
if '':
    print('빈문자열은... 빈문자열...?')
else:
    print('아무일도 벌어지지 않음')

빈 리스트 == False
my_list = ['가', '나', '다']


print(sum(my_list))  는 에러
my_list = [[1, 2, 3], [4, 5]]
print(sum(my_list, [])) #[1, 2, 3, 4, 5]

for else
while else
빈 리스트 호출 조심

numbers = []
numbers += [1]
#[1]
```py
numbers_words = [
    '1 2 3 4 5',
    '6 7 8 9 10',
    '11 12 13 14 15'
]
# 최종결과물
numbers = []
for words in numbers_words:
    conversion_list = list(map(int, words.split()))
    numbers.append(conversion_list)
print(numbers)

numbers = [1, 2, 3, 4]
numbers = [list(map(int, words.split())) for words in numbers_words]
numbers = [[0] * 10 for _ in range(10)]
numbers = [[0 for _ in range(10)] for _ in range(10)]
print(numbers)
```

함수를 정의할 때, 매개변수에 패킹을 사용해서
가변 인자로 받게 되면 튜플로 받는데...

왜, 변수에 패킹을 사용해서
다수의 데이터를 받으면 리스트로 받는 이유는 뭔가요?
print([1, 2, 3, 4, 5])
print(*[1, 2, 3, 4, 5])

lambda n(매개변수,매개변수): 함수할일

```py
def my_sum(num1, num2):
    return num1 + num2
result = my_sum(1, 2)

my_sum_lambda = lambda num1, num2: num1 + num2
result_2 = my_sum_lambda(3, 4)
print(result, result_2)

a = [1, 2, 3]
b = [4, 5, 6]
result_3 = map(lambda num1, num2: num1 + num2, a, b)
print(list(result_3))

result_4 = map(my_sum, a, b)
print(list(result_4))
```

# 파이썬 함수의 특징
    # 파이썬 함수는 반드시 반환하는 값이 하나의 객체이다.
    # 그런데, 만약 2개 이상의 객체를 반환하도록 하려고하면,
    # 파이썬이 알아서 tuple로 묶어서 반환한다.

def reverse_string(word):
    # reversed 함수는?
    # return list(reversed(word))
    return ''.join(reversed(word))

빈 문자열에 붙이는 식도 ㄱㅊ
```py
def even_elements(arr):
    result = []
    tmp = []
    # 전체 리스트의 요소를 순회
    # 리스트에 값이 있는 동안 순회
    while arr:
        # 0번째 요소를 pop -> pop에 인자를 안넣으면 뒤에서부터 제거
        # -> 리스트의 순서가 바뀔 수 있음.
        element = arr.pop(0)
        # 각 요소들을 하나씩 뽑아, 짝수인 경우에만
        if element % 2 == 0:
            # 임시변수 tmp에 추가
            tmp.append(element)
    # extend는 순회 가능한 요소를 모두 순회하며 리스트에 추가하는 메서드
    result.extend(tmp)
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
```

문자열은 반환값이 대체로 있다

counut_dict = {i: 0 for i in range(1, 10)}

```py
# 아래 함수를 수정하시오.
def remove_duplicates_to_set(arr):
    return set(arr)
# 가정 : arr에 1~9 까지의 정수만 요소로 삽입된다면,
def remove_duplicates_to_set(arr):
    # 기본 dict # 첫 초기화는 0번 나왔다고 초기화
    # counut_dict = {1: 0, 2: 0, 3: 0, 4: 0}
    # dict_comprehension
    counut_dict = {i: 0 for i in range(1, 10)}
    # return counut_dict
    # 중복이 없다.
    # 배열의 모둔 요소를 순회한다.
    # 이떄, 순회 대상이, 이전에 한번도 나온적이 없다.
        # 요소를 중심으로 해당요소가 몇번 나왔는지 셀 수 있어야함.
        # 1이 1번 나왔으면 1=1
        # 2가 3번 나왔으면 2=3
        # dict = {1: 1, 2: 3}
    for num in arr:
        counut_dict[num] += 1
    # 모든 출현횟수 기록해둔 dict를 순회해서
        # value가 1인 (1번 이상 나온 값) key 모아서 새 list
    result = [key for key, item in counut_dict.items() if item >= 1]
    return set(result)

# 가정 : arr에 1~9 까지의 정수만 요소로 삽입된다면,
def remove_duplicates_to_set(arr):
    count_list = [0 for i in range(10)]
    for index in arr:
        count_list[index] += 1
    result = [num for num in range(len(count_list)) if count_list[num] >= 1] 
    return result

# 딕셔너리에 집중
def remove_duplicates_to_set(arr):
    # 최종 결과물
    result = set()
    duplicate_check_dict = {}
    for num in arr:
        # 해당하는 키가 dict에 없다면
        # if dict.get(key) == None:
        #     dict[key] = 0
        # else:
        #     dict[key] += 1
        # if dict[key]: (키가 없는경우 KeyError)
        duplicate_check_dict[num] = duplicate_check_dict.get(num, 0) + 1
        # 중복없음 == 1번만 나왔으면 아무튼 나온거임
        if duplicate_check_dict[num] == 1:
            result.add(num)
    return result

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
``` 약간 카운팅정렬 느낌이네

```py
data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
# 가장 기본적인 dict 순회
for key in data:
    print(key, data[key])

# items() => [(key, value), (key, value)]
for item in data.items():
    print(item) # (key, value)
    key, value = item
    print(key, value)

# items() => [(key, value), (key, value)]
for key, value in data.items():
    print(key, value) # (key, value)

print(data.keys())
# for key in data:
# for key in data.keys():
#     print(key)



# 2. data가 가진 벨류 목록들만 모아서 출력한다.
print(data.values())

# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
# data가 가진 모든 값 순회
# for key in data:
#     # 순회도중 key의 값이 without이라면
#     if key == 'without':
#         # 근데 그 키가 있다면,
#         if data.get(key):
#             # value 출력
#             print(data[key])
#         # 없다면
#         else:
#             # 특정 문자열 출력
#             print('unknown')
print(data.get('without', 'unknown'))
    
# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
data.update(plus_data)
print(data.update(plus_data))
# for key in plus_data:
#     data[key] = plus_data[key]

# 5. 변경된 data를 출력한다.
print(data)
```
```py
print("""
      usage: thingy [OPTIONS]
      -h
      -H hostname
      """)

print('Py' 'thon')
#'Python' 변수나 표현식에는 적용불가,+로 해야됨.  오직 두개의 리터럴만. 
```
문자열에 너무 큰 인덱스 호출은 에러, but 슬라이싱에서는 부드럽게 처리
슬라이싱은 얕은 복사본을 리턴
리스트에서 슬라이싱으로 내용변경, 내용삭제_길이변경, 초기화 등 가능

for  _ in range(len(n_list)) 같은 반복문에서 n_list를 수정하면 길이 변경
복사본을 만들거나 새 컬렉션 만들어라

for - else 문에서 else는 break가 발생하지 않을 때 실행됨
for n in range(2,2):
    print(n)         출력 x
        

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _: #예외처리
            return "Something's wrong with the internet"

print(http_error(400)) # switch 느낌

case 401 | 403 | 404:
    return "Not allowed"
  
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

함수는 return이 없으면 None을 출력

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
^
|
v
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

해법
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw]) 매개변수에서는 패킹

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

딕셔너리 언패킹 시 a:b -> a=b

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
42
f(1)
43

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
sort()의 key매개변수를 이용해 두번째 요소를 기준으로 졍렬
```py
a = [1,2,3]
a[len(a):] = [4] # append()
a[len(a):] = [4,5,6] # extend()
a[len(a):] = {5,7,8}
a[len(a):] = {10:1,20:5}


print(a)
``` 리스트에 세트를 append하면 랜덤하게 값이 리스트로 들어감. 딕셔너리는 key값만

remove()는 첫번쨰 만나면 삭제, 없으면 ValueError
index(x)는 첫번째 만나는 x 인덱스 반환. 없으면 ValueError
copy()는 얕은 복사, a[:] 와 동등
list.sort(*, key=None, reverse=False)

형이 다르면 정렬되지 않는다. 에러뜸

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
squares = list(map(lambda x: x**2, range(10)))

리스트 컴프리헨션 시 반환값이 2개 이상이면 튜플로 묶어줘야됨

리스트 컴프리헨션으로 전치하기
[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

del문. 인덱스를 없애버림. 리스트 초기화도 가능. 리스트를 참조했다는 것도 삭제가능

singleton = 'hello', #튜플로 만들기

x,y,z = t

a = {x for x in 'abracadabra' if x not in 'abc'}
a
{'r', 'd'}

list(딕셔너리)sms key값들 리스트로 반환

a = dict([{'sape', 4139}, ('guido', 4127), ('jack', 4098)])
print(a) 
#2개의 요소로 되어있으면 출력. 세트면 랜덤. 리스트나 튜플은 그대로. 딕셔너리일 경우 key를 가져오기 때문에 2쌍의 key로 key:value 설정. sape=4139같은 형식도 가능

zip()

import fibo as fib
#닉네임 설정
format() 메서드
print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
ㄷ
nonlocal은 한단계 위에?

x.f()는 정확히 MyClass.f(x) 와 동등합

클래스변수에 리스트가 오면 인스턴스에서 클래스변수를 호출하고 수정가능해짐. 인스턴스 변수로 설정해야함. 유의