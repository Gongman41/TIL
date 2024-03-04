```py
N = int(input())
lst = [[0]*7 for _ in range(2)]
for n in range(4)
  lst[0][n] = N+n
  lst[1][7-n] = N-n
lst = str(lst)
print(*lst)
```
O log n
알고리즘에서 log의 밑수는 2
2의 몇 승이 되는 지 추정. 올림함  .
O(1) 보단 느리지만 유사한 성능
O(NlogN)_sort 은 O(logN)_이진탐색보다는 느리지만 비슷한 성능

16진수. 2진수를 더 가독성 있게 사용
2진수를 10진수로 변환시 연산 오래걸림
2진수를 16진수로 변환시 연산속도 매우빠름

윈도우 + r + calc
HEX 16진수
DEC 10진수
OCT 8진수
BIN 2진수

10진수 2로 나눈 나머지 거꾸로하면 2진수

2진수 16진수 변환은 연산이 없음. 라이브러리 사용이나 단순 암기

##비트연산
- 1bit: 0과 1을 표현하는 정보의 단위
- 1Byte: 8 bit를 묶어 1Byte라고 한다.
- 비트연산: 컴퓨터의 CPU는 0과 1로 다루어 동작. 내부적으로 비트연산을 사용해서
    덧셈 뺄셈등 진행
  - &:비트단위로 AND연산을 한다
    - 2진수에서 같은 것만 살림
  - |:비트단위로 or연산을 한다
    - 2진수에서 살릴 거 다 살림
  - ^:xor연산자. 같으면 0, 아니면 1  
    - xor 두번하면 원래 수로 돌아옴, 암호화에 사용
- 2진수_0b를 접두어
- 10진수_0x를 접두어
- 16진수: 0xBB3


bin() 2진수로, hex()16진수로, int(,) 10진수로
 

  - '<<':피연산자의 비트 열을 왼쪽으로 이도ㅓㅇ
  - '>>':파연산자의 비트열을 오른쪽으로 이동
    - 1 << n : 2^n
    - i & (1<<n) : 같거나 작은 수? i의 n번 비트가 1인지 아닌지 확인할 수 있다.
    - 음수 표현 방법: 음수를 2의 보수로 관리. 맨 앞자리 bit는 음수 or 양수를 구분하는 비트
        - 뺄셈의 연산속도 굿, 0과 -0을 따로 취급하지 않기때문
        - MSB = 1(음수), 아니면 양수
        - 표현방법: 수를 모두 뒤집고 + 1
        - 2의 보수를 두번 취하면 원래의 값으로 돌아옴
  - Not 연산자
    - (~): 모든 비트를 반전시킨다 _ 이걸로 보수 생성?
        - ~4는 -5
```python
N,M = map(int,input().split())
check = True
for n in range(1,N+1):
    if not (M & (1<<n)):
        check =False
if check == True:
    print('ON')
else:
    print('OFF')
```    
- 파이썬에서 실수 출력 방법
    - 파이썬은 f-string 문법을 지향
    - {t:.nf} n자리까지 반올림
    - 파이썬은 굉장히 넓은 범위의 실수 표현가능
    - +로 넘어가면 inf, -로 넘어가면 0으로 표현
    - print(0.1+0.1+0.1 == 0.3) #False
      - 실수를 내부적으로 근사적으로 관리. 소수점이 있는 10진수를 2진수로 변환할 경우 문제 발생. 반올림 사용?
```python
t = 0.1
print(f'{t:.20f}')
```

- 소수점이 있는 10진수를 2진수로 변환할 때
  
   

##실수
근사값으로 저장

## 투포인트 알고리즘
-  a = 맨처음
-  b = 중간 + 1
-  loop{
-  a 출력 후 a += 1
-  b 출력 후 b += 1
-  }

## 재귀호출
- 반복문은 코드를 n번 반복
- 재귀호출은 n 중 반복문 만들기. 하나의 문제를 더 작은 문제로 쪼개기
- 함수 호출 시 int타입 객체를 전달하면 값만 복사된다
-  기저조건: 무한 재귀호출을 막는 것,깊이
- 재귀호출코드의 개수가 브랜치 개수
## 완전탐색
- 순열: 서로 다른 N개에서 R개를 중복없이 순서를 고려하여 나열하는것
- 중복순열: 중복 가능 순열
    - 재귀호출을 할 때마다 이동경로를 흔적으로 남긴다
    - 가장 마지막 레벨에 도착했을 때  이동경로를 출력한다
    - print는 마지막 레벨에 도착했을 때 출력
    - 이동할 곳의 위치를 path리스트에 기록
```python
path = []

def KFC(x):
    if x == 2: # 값 개수
        print(path)
        return
    for i in range(3): #나올 수 있는 값의 개수
        path.append(i)
        KFC(x+1)
        path.pop()
KFC(0)
```    
- 중복을 취급하지 않는 순열 구현방법
    - 중복순열 코드를 작성한다
    - 중복을 제거하는 코드를 추가하면 순열 코드 됨
    
- 중복 제거 원리
    - 전역리스트를 사용하면 이미 선택했던 숫자인지 아닌지 구분할 수 있다
    -  이를 used,visited 배열이라고 함
    - 재귀호출을 하기 직전 이미 선택했던 숫자인지 검사하는 코드 필요
```python
used = [False, False, False] #브랜치 개수
path = []

def KFC(x):
    if x == 2:
        print(path)
        return
    for i in range(3):
        if used[i] == True:continue
        used[i] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i] = False
KFC(0)
```    

```py
path = []
cnt = 0
def kfc(x,sum):
  global cnt
  if sum > 10:
    return
  if x == 3:
    cnt += 1
    return
  
  for i in range(1,7):
    path.append(i)
    kfc(x + 1, sum +i)
    path.pop()

kfc(0,0)
print(cnt)
```
```py
card = ['A','J','Q','K']
path = []
cnt = 0

def cont_three():
  if path[0] == path[1] == path[2] : return True
  if path[1] == path[2] == path[3] : return True
  if path[2] == path[3] == path[4] : return True
  return True

def permu(lev):
  global cnt
  if lev == 5:
    if cont_three() : cnt += 1
    return
  
  for i in range(4):
    path.append(card[i])
    permu(lev+1)
    path.pop()

permu(0)
print(cnt)
```
카트 배열최소합
## 부분집합,조합/그리디
- 부분집합 찾기
  - 완전 탐색(학습용)
    중복순열로 풀기

```py
arr = ['O','X']
path = []
name = ['MIN','CO','TIM']

def print_name():
  print('{', end = '')
  for i in range(3):
    if path[i] == 'O':
      print(name[i], end = ' ')
  print('}')

def run(lev):
  if lev == 3:
    print_name()
    return
  
  for i in range(2):
    path.append(arr[i])
    run(lev + 1)
    path.pop()

run(0)
```
  -  binary counting(실전용)
    원소 수에 해당하는 N개의 비트여ㅑㄹ을 이용

```python
arr = ['A','B','C']
n = len(arr)
def get_sub(tar):
    for i in range(n):
        if tar & 0x1: #0b110이 주어지면 BC 출력하는 함수
            print(arr[i],end='') #첫번째 자리가 1이면 해당 함수 출력
        tar >>= 1# 검사한 한 자리를 제거

for tar in range(1<<n):
    print('{',end='')
    get_sub(tar)
    print('}')
```     
```python
arr = ['A','B','C','D','E']
n = len(arr)

def get_count(tar):
  cnt = 0
  for i in range(n):
      if tar & 0x1: #1비트가 1인지 확인하는 코드
        # 십진수로 써도 가능은 한데 가독성문제
          cnt+= 1
      tar >>= 1#체크하고 밀고
    # right_shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
  return cnt
result = 0
for tar in range(1<<n):
  if get_count(tar) >= 2:
    result += 1
print(result)
```     

- 순열과 조합 차이
  조합: 서로 다른 n 개의 원소를 순서없이 골라낸 것
```python
arr = ['A','B','C','D','E']
path = []

def run(lev,start):
  if lev == n:
    print(path)
    return
  for i in range(start,5):
    path.append(arr[i])
    run(lev +1, i+1)
    path.pop()

run(0,0)
```

```python
N = 3
path = []

def func(lev, start):
    if lev == N:
        print(path)
        return
    for i in range(1,7):
        path.append(i)
        func(lev + 1, i)
        path.pop()
func(0)
```

## 그리디
```python
person = [15,30,50,10]
n = len(person)
person.sort()
sum = 0
left_person = n -1
```
```python
target = 30
things = [(5,50),(10,60),(20,140)]

things.sort(key = lambda x : (x[1]/x[0]), reverse = True)

sum = 0

for kg, price in things:
    per_price = price/kg
    if target < kg:
        sum += target * per_price
        break
    sum += price
    target -= kg
print(int(sum))
```
