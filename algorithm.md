## 시간복잡도
- 실제 걸리는 시간 vs 실행되는 명령문의 개수

## 빅-오(O)표기법.
- 시간 복잡도 함수 중에서 n에 대한 항만 표쇼시
    - 계수는 생략
    O(3n+2) = O(n)
    O(4) = O(1)
    O(nlog n) 의 시간 복잡도 굉장히 낮음

## 배열
- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
- 배열이 가리키는 연속된 메모리의 주소에 데이터(의 주소) 저장
- 다수의 변수로 처리하기 힘든 작업 시행 가능

## 정렬
- 버블 정렬(O(n^2)): 인접한 원소를 비교하며 자리를 계속 교환하는 방식
    - 나머지끼리 다시 정렬
    - 비교와 교환
    for i: N-1 -> 1
      for j: 0 -> i-1
        if a[j] >a[j+1]
            a[j] <-> a[j+1]
```py
def BubbleSort(a,N):
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
```
      
# 카운팅 정렬
- 정수나 정수로 표현할 수있는 자료에 대해서만 적용가능.
- 정수 항목으로 인덱스되는 카운트들의 배열을 사용하기 때문
  - 시간복잡도 O(n+k): n은 리스트 길이, k는 정수 최대값
  - 앞에 위치할 항목의 개수를 반영하기 위해 counts 원소 조정 가능
  - 오른쪽부터 차례대로 나오는 요소의 counts를 -시키면서 count 인덱스에 요소를 추가
  - 앞에서 부터 정렬 시 지리 바뀜. 좌표같은 값일 경우 문제발생.
```python
    N = 6
    K = 9
    data = [7,2,4,5,1,3]
    counts = [0]*(K+1)
    temp = [0]*N
    for x in data:
        counts[x] += 1
    for i in range(1,K+1):
        counts[i] = counts[i-1]+ counts[i]
    for i in range(N-1,-1,-1):
        counts[data[i]] -= 1
    temp[counts[data[i]]] =  data[i]
    print(*temp)
```
```py
def Counting_Sort(DATA,TEMP,k):
# DATA []--입력 배열(0 to k)
# TEMP []--정렬된 배열
# COUNT [] -- 카운트 배열
    COUNTS = [0]*(k+1)
    for i in range(0,len(DATA)):
        COUNTS[DATA[i]] += 1
    for i in range(1,k+1):
        COUNTS[i] += COUNTS[i-1]
    for i in range(len(TEMP)-1,-1,-1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]
```
## 완전검색
- 모든 경우의 수를 나열해보고 확인하는 기법
- 경우의 수가 상대적으로 작을 때 유용
- 수행속도 느림, 해답 찾아내지 못할 확률이 낮음
- 브루트포스

## 순열
- 서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열하는 것
- nPr = n* ... (n-r+1)
```python
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i3 and i3 != i2:
                    print(i1,i2,i3)

```
최종적으로는 재귀로

## 탐욕 알고리즘
- 최적해를 구하는 데 사용되는 근시안적인 방법
- 지역적으로는 최적, 하지만 그것이 최종적으로 최적이라는 보장은 없음
- 일반적으로 떠오른 생각 그냥 구현하면 greedy한 구현
    - 거스름돈 줄이기
    
baby_gin 카운팅배열로 풀기

```python
num = 456789
c = [0]*12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num%10] += 1
    num //= 10
```

## 2차원 배열
  - 차원에 따라 index를 선언
  - 파이썬에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함

```python
N = int(input())
arr = (list(map(int,input().split())) for _ in range(N))
```
공백으로 구분

```python
N = int(input())
arr = (list(map(int,input())) for _ in range(N))
```
```python
N = int(input())
arr = (list(map(int,input())) for _ in range(N))
arr2 = [[0]*N for _ in range(N)]
# arr3 = [[0]*N]*N 얕은 복사. 요소 값 바꾸면 다같이 바뀜
```

  - 배열 순회
    - n * m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법
행 우선 순회
```python 
  for i in range(n):
    for j in range(m):
      f(arr[i][j])

``` 
열 우선순회는 반대로
    - 지그재그 순회
```python
for i in range(n):
    for j in range(m):
        f(array[i][j+(m-1-2*j)*(i%2)])
```

  - 델타를 이용한 2차 배열 탐색.
    - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법.
    - 인덱스 (i,j)인 칸의 상하좌우 칸 (nj,ni)
    ```python
    dj = [1,0 ,-1, 0]
    di = [0,1,0,-1]
    N = 5
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0 <= nj<N:
                    print(arr[ni][nj], end = ' ')
                print()
    ```
    뺄거를 리스트로 만들어서 현재위치에서 순회ㅏ
```python
N = 5
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni,nj = i+di,j+dj
                if 0<=ni<N and 0 <= nj<N:
                    print(arr[ni][nj], end = ' ')
                print()
```

  - 전치 행렬
```python
arr = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
```

## 부분집합 합
- 유한 개의 정수로 이루어진 집합이 있을 때 이 집합의 
  부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이
  되는 경우가 있는 지를 알아내는 문제
  - 완-탐: 모든 부분집합 생성 후 계산
    - 2^n개의 부분집합.
  ```python
  bit = [0,0,0,0]
  for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for i in range(2):
                bit[3] = i
                print_subset(bit)
  ```
### 비트 연산자
  - 상태를 구분할 수 있는 최소 단위. 비트단위로 연산
  - &,|,<(왼쪽으로 이동),>(오른쪽으로 이동)
  - << 연산자: 1<<n: 2^n 즉 원소가 n개일 경우의 모든 부분집합의 수를 의미
  - & 연산자: i&(1<<j): i의 j번째 피트가 1인지 아닌지를 검사한다
간결하게 부분집합 생성방법
```python
arr = [3,6,7,1,5,4]
n = len(arr)
for i in range(1<<n): # 부분집합의 개수. bit연산자로 1을 2진수로 바꾸기
    s = 0
    for j in range(n):#원소의수만큼 비트를 비교함
        if i & (1<<j):#i의 j번 비트가 1인 경우
            s += arr[j ]
            print(arr[j],end = ",")
    print()
print()
```
뭔소린가
```python
def f(arr,N):
    for i in range(1, 1<<n): # 부분집합의 개수
        s = 0
        for j in range(n):#원소의수만큼 비트를 비교함
            if i & (1<<j):#i의 j번 비트가 1인 경우
                s += arr[j]
        if s == 0:
            return True
        return False

N = int(input())
arr = list(map(int,input().split()))
print(f(arr(arr, N)))
```
## 검색
 - 목적하는 탐색 키를 가진 항목ㅇ믈 찾는것
### 순차 검색
- 가장 간단하고 직관적인 검색방법. 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용
- 검색 대상의 수가 많은 경우 수행시간이 급격히 증가하여 비효율저ㅗㄱ
    - 정렬되어 있지 않은 경우정렬되어 있는 경우
      - 첫번째 원소부터 순서대로 검색대상과 키 값이 같은 원소가 있는 지 비교하며 찾는다
      - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스 반환.
      - 자료구조의 마지막에 이를 때까지 검색대상을 찾지 못하면 검색실패  
      - A[-1] == current
        return -1
        
    - 정렬되어 있는 경우
      - 찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
      - 평균 비교 회수: (1/n)*(1+2+3+...+n) = (n+1)/2
      - O(n), 실패시에도 O(n)
```python
def sequential_search(a,n,key)
    i = 0
    while i < n and a[i]!= key: #인덱스 에러, and 연산: 앞에 False면 뒤에 연산 안함(if느낌)
        i += 1
    if i < n:
        return i
    else:
        return -1
```

      - 중간에 있어야할 위치에 없으면 -1 리턴

```python
def sequential_search2(a,n,key):
    i = 0
    while i < n and a[i]!= key: #인덱스 에러, and 연산: 앞에 False면 뒤에 연산 안함(if느낌)
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1
```

## 이진 검색
    - 자료 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정
    하고 검색을 계속 진행하는 방법
        - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색범위
        를 반으로 줄여가면서 보다 빠르게 검색을 수행
        - 자료가 정렬된 상태여야 한다.
    - 검색과정
        - 자료의 중앙에 있는 원소를 고른다
        - 중앙 원소의 값과 찾고자 하는 목표값을 비교한다
        - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서ㅗ
        새로 검색을 수행, 크다면 오른쪽 반에 대해서 새로 검색을 수행
        - 찾고자 하는 값을 찾을 때까지 반복
    - 구현
        - 검색범위의 시작점과 종료점을 이용하여 검색을 반복 수행한다.
        - 이진 검색의 경우 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬
          상태로 유지하는 추가 작업이 필요

```python
def binarySearch(a,N,key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

```

## 인덱스
    - 테이블에 대한 동작속도를 높여주는 자료구조
    - 인덱스를 저장하는 데 필요한 디스크 공간은 보통 테이블을 저장하는 데
    필요한 디스크 공간보다 작다_ 키-필드만 가지고 있고 테이블의 다른 세부항목들은 갖고있지 않기 때문
    - 배열을 사용한 인덱스
        원본 데이터 배열에 배열 인덱스 추가 시 상대적으로 크기가 작은 인덱스
        배열을 정렬하기 때문에 속도가 빠르다

 - 선택정렬: 가장 작은 것부터 골라서 차례대로 정리
    - 주어진 리스트 중에서 최소값을 찾는다
    - 그 값을 리스트의 맨 앞에 위치한 값과 교환
    - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복
    - O(n^2). 교환횟수가 버블, 삽입정렬보다 작다. 대신 K가 비교적 작을 때만 가능
```python
def SelectionSort(a,N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
```
    
 - 셀렉션 알고리즘
    - 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
    - 최소값, 최대값, 혹은 중간값을 찾는 알고리즘
    -선택과정
        - 정렬알고리즘을 이용하여 자료 정렬하기
        - 원하는 순서에 있는 자료 가져오기
    - 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고
    배열의 k번째를 반환한다
    - k 가 비교적 작을 때 유용. O(kn)의 수행시간

```python
def Select(arr,K):
    for i in range(0,K):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[K-1]
```
 

## String
### 코드체계
    - 메모리는 숫자만을 저장할 수 있기 때문에 각 문자에 대해서 대응되는 숫자를 정해놓고 이것을 메모리에 저장. 6비트면 영어 모두 표현
    - 지역마다 정보해석에서의 차이 발생, ASCII라는 문자 인코딩 표준 제정
    - 확장 아스키는 추가적인 문자 표현가능하지만 서로 다른 프로그램이나 컴퓨터 사이 교환 불가
    - 각 나라 언어를 적용한 코드체계 발생, 다국어 처리를 위한 표준 따로 마련. 유니코드.
    - 유니코드는 character set으로 분류, 변수의 크기를 정의. 하지만 바이트 순서에 대해서 표준화 못함. 따라서 파일을 인식 시 이 파일이 UCS-2인지, UCS-4인지 인식하고 각 경우를 구분해서 모두 다르게 구현. 유니코드의 적당한 외부인코딩 필요_UTF-8,UTF-16,UTF-32
    - 파이썬은 UTF-8_생략가능. 다른 인코딩 방식으로 처리 시 따로 지정
### 문자열
    - 자바에서 String: 기본적인 객체 메타데이터외에도 hash값, 문자열 길이(count), 문자열 시작점(offset), 실제 문자열 배열에 대한 참조(value)
    - C언어에서 문자열 처리: 문자들의 배열형태로 구현된 응용자료형. 문자배열에 문자열을 저장할 때는 항상 마지막에 끝을 표시하는 널문자(₩0)을 넣어줘야 한다
    - Java(객체지향 언어)에서의 문자열 처리: 문자열 데이터를 저장, 처리해주는 String클래스 사용. 연산자 메서드 형태로 제공
    - python에서의 문자열 처리: char 타입 없음. 텍스트 데이터의 취급방법이 통일되어 있음.' ," ,''' ,""", +(문자열 연결),*(문자열 반복)

    - C와 Java String 처리의 기본적인 차이점.
        - C는 아스키 코드로 저장
        - Java는 유니코드(UTF-16,2byte)로 저장
        - 파이썬은 유니코드(UTF-8)로 저장
    - 문자열 뒤집기: 자기 문자열에서 뒤집기, 새로운 빈 문자열을 만들어 소스 뒤에서부터 읽어서 타겟에 쓰는 방법
        - 자기 문자열을 이용할 경우 swap을 위한 임시 변수가 필요, 반복수행을 문자열 길이의 반만을 수행
    - 문자열 비교: C strcmp(), Java equals(), python == or is.
    - 문자열 숫자를 정수로 변환
        - C atoi(), Java parse 메서드, python 숫자와 문자변환 함수
### 패턴매칭
     - 고지식한 알고리즘: 처음부터 끝까지 차례대로 순회, 일일이 비교
```python
p = "is" #찾을 패턴
t = 'This is a book~!'
M = len(p)
N = len(t)

def BruteForce(p,t):
    j = 0
    i = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i+1
        j = j + 1
    if j == M : return i - M
    else: return -1
```
최악의 경우 O(MN)

### KMP 알고리즘
- 매칭이 실패했을 때 돌아갈 곳을 제한. 불일치 발생지점 전까지의 문자는 알고있으므로 다시 비교 x. 패턴을 전처리하여 배열 next[M]_불일치가 발생했을 경우 이동할 다음 위치_을 구해서 잘못된 시작을 최소화. O(M+N).
- 찾을 문자열이 일정한 패턴을 가질 경우 효과적으로 적용 가능. 
    

### 보이즈 무어
- 오른쪽에서 왼쪽으로 비교
- 패턴에 오른쪽끝에 있는 문자가 불일치하고 이 문자가 패턴내에
존재하지 않는경우 이동거리는 패턴의 길이만큼이 된다. 현재 탐색중엔 구간내에 찾는 문자열내에 문자가 존재하는 경우 해당 문자로 맞춰 이동.
- 최악의 경우 O(MN)
  
### 문자열 암호화
# 스택
 - 특성: 자료를 쌓아올린 형태의 자료구조
    - 스택에 저장된 자료는 '선형구조'를 갖는다
        - 자료간의 관계가 1대1의 관계를 갖는다
        <-> 비선형구조:1대N(트리)
        스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있음
    - 후입선출
 - 구현
    - 자료구조: 자료를 선형으로 저장할 저장소
        - 배열 사용
        - 저장소 자체를 스택이라 부르기도 함
        - 맨 위 요소를 top이라 함
    - 연산: 삽입(push), 삭제(pop),isEmpty, peek(top 원소 반환)
        - 공백일 경우 top = None. 인덱스를 가리키는 변수
    
 ```python
while top >= 0
top -= 1
tmp = stack(top+i)

``` 
```python
def push(n):
    global top
    top += 1
    if top == size:
        print("overflow")
    else:
        stack[top] = n
        
top = -1
size = 10
stack = [0]*10
```
```python
top += 1
stack[top] = 10

while top >= 0
    top -= 1
    print(stack[top+1])
```
pop은 top만 변경. size가 고정되어 있기도 하고, 굳이 초기화 안해도 되기도 하고

- 스택구현 고려사항
    - 1차원 배열을 사용하여 구현 시 구현 용이, but 스택 크기 변경 어렵
    - 동적 구현: 그냥 우리가 하던 거
- Funtion call: 마지막에 호출된 함수가 먼저 실행. 후입선출구조로 수행 순서관리
    - 함수 호출 발생 시 해당 지역 변수, 매개변수 및 수행 후 복귀할 주소등의 정보를 스택 프레임에 저장하여 시스템 스택에 삽입
- 재귀 호출: 프로그램의 크기 줄이기. But 중복호출 발생

    
## Memoization
    - 재귀호출 내 중복호출.
    - 이전에 계산한 값을 메모리에 저장해 계산 빠르게. memo[0]이나 memo[1]의 값이 중복호출 많이 발생하기 때문에 따로 저장
    - 동적 계획법의 핵심 O(2^n) 에서 O(N)까지 줄이기 가능
```python
def fibo1(n):
    global memo  
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]
memo = [0]*(n+1)
memo[0] = 0
memo[1] = 1
```
## DP
 - 동적계획법: 최적화 문제를 해결하는 알고리즘
    - 작은 부분 문제들을 해결하고 그 해를 이용해 큰 크기의 부분문제를 해결
    - 완전탐색을 효율적으로 하는 느낌
    - memoization울 재귀적 구조에 사용(함수 호출,사용하는데 시간 오래 걸림)하는 것보다
    Dp를 반복적 구조로 구현한 것이 성능면에서 효율적이다
        - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문  
        - 최대 호출 깊이.
    
## DFS
 - 비선형 구조인 그래프 구조는 그래프로 표현된
    모든 자료를 빠짐없이 검색하는 게 중요
    - DFS:깊이 우선 탐색: 여러 자료구조에서 사용가능
      - 깊게 가다가 갈림길(스택으로 저장)로 다시 왔다갔다 왔다.
      - 안가본 곳, 지금 위치 push하고 내려감, 다 가봄, pop하고 받은 정점으로 이동,다시 반복  
      - 정점,간선 
    
```python
def dfs(i):
    visited = [0]*(V+1)
    st = []
    visited[i] = 1 #시작점 방문
    print(i)
    while True: # 탐색
        for w in adji[i]:
            if visited[w] == 0:
                st.append(i) # push(i), i를 지나서 w에 방문
                i = w            
                visited[i] = 1
                print(i)
                break
        else:       # i에 남은 인접 정점이 없으면
            if st: # 스택이 비어있지 않으면(지나온 정점이 남아 있으면)
                i = st.pop()
            else: # 스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break
    # visited, stack 생성 및 초기화
V,E = map(int,input().split())
arr = list(map(int,input().split()))

adji = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2],arr[i*2+1]
    adji[n1].append(n2)
    adji[n2].append(n1) # 방향이 없는 경우_
dfs(1,V)
```
 반복문으로
```python
def dfs(i):
    visited[i] = 1 #방문표시
    print(i) # 출력
    #i에 인접하고 방문안한 w가 있으면
    for w in adji[i]:
        if visited[w] == 0:
            dfs(w)
    
    # visited, stack 생성 및 초기화
V,E = map(int,input().split())
arr = list(map(int,input().split()))

adji = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2],arr[i*2+1]
    adji[n1].append(n2)
    adji[n2].append(n1) # 방향이 없는 경우_
visited = [0]*(V+1)
dfs(1,V)
```
 재귀로. 하지만 깊이제한때문에 반복으로
 간선의 계수 유의.

- BFS:너비 우선 탐색

## 계산기
    - 문자열 수식 계산
        - 중위 표기법: 연산자를 피연산자의 가운데 표기하는 법
        - 후위 표기법: 연산자를 피연산자 뒤에 표기하는 방법 (AB+)
            - 변환 방법: 괄호를 사용하여 다시 표현
            - 입력받은 중위표기식에서 토큰을 읽음 -> 토큰이 피연산자이면 토큰을 출력 or 토큰이 연산자(괄호포함)일 때 스택의 top에 저장되어있는 연산자보다 우선순위가 높으면 push, 아니면 우선순위가 작아질때까지 pop한다음 토큰의 연산자를 push. top에 연산자가 없으면 그냥 push -> 토큰이 오른쪽 괄호이면 top에 왼쪽괄호가 올 때까지 스택에 pop하고 pop한 연산자 출력. 왼쪽괄호 만나면 pop만하고 출력하진 않음. -> 중위표기식에 더 읽을 것이 없으면 중지, 있으면 1부터 다시 반복 -> 스택에 남아있는 연산자를 모두 pop하여 출력. 스택밖의 왼쪽괄호는 우선순위가 가장 높으며 스택안의 왼쪽괄호는 우선순위가 가장 낮다

    
```python
st = input()
stack = [0]*len(st)
top = -1
pee_list = list(map(str,range(0,10)))
yonsan_dict = {"+":1,"-":1,"%":2,"*":2,"**":2,"(":0,")":0,"/":2,"//":2}
for s in st:
    if s == ' ':
        pass
    elif top == -1:
        stack.append(s)
        top += 1
    elif s in pee_list:
        print(s,end=" ")
    elif s == ")":
        while stack[top] != "(":
            print(stack.pop(),end=" ")
            top -= 1
        stack.pop()
        top -= 1
    else:
        if yonsan_dict[s] > yonsan_dict[stack[top]]:
            stack.append(s)
            top += 1
        else:
            while yonsan_dict[s] <= yonsan_dict[stack[top]]:
                print(stack.pop(),end = " ")
                top -= 1
            stack.append(s)
            top += 1
while stack:
    print(stack.pop(),end = " ")
```

## 계산기 2
- 피연산자를 만나면 스택에 push , 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push한다, 수식이 끝나면 마지막으로 스택을 pop하여 출력
- 연산자 나오면 top, top-1 인덱스의 피연산자로 연산

## 백트래킹
-  해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아가는 기법(DFS?)
- 최적화문제와 결정문제(문제의 조건을 만족하는 해가 존재하는지 여부를 yes or no)를 해결가능
    - 미로찾기
    - n-Queen
    - Map coloring
    - 부분집합의 합 문제 등
- DFS와의 차이: DFS는 모든 경로를 추적, 백트래킹은 불필요한 경로를 조기에 차단. 경우의 수를 줄일 수 있지만 최악의 경우에는 여전히 지수함수 시간을 요함
    - 특정 노드의 유망성 점검 후 유망하지않으면 노드의 부모로 돌아가 다음 자식노드로.
    - 유망성은 해답일 가능성으로 측정.
    - 가지치기: 유망하지 않은 노드가 포함되는 경로는 더 이상 고려하지 않음
- 깊이우선검색 실시 -> 유망성 점검 -> 유망하지 않으면 부모노드로 돌아가 검색 계속

# 퀵정렬, 분할정복


























## Queue
### 큐
    선형큐에서 front를 마지막으로 삭제된 인덱스로.
    - 선입선출 FIFO

```python
N = 10
q = [0]*10
front = rear = -1
def enqueue(item):
```

## BFS
    - 그래프를 탐색하는 방법에는 크게 두가지
        - 깊이 우선 탐색(DFS)
        - 너비 우선 탐색(BFS)
    - 너비우선탐색은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한  후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식??
    - 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, 선입선출 형태의 자
        료구조인 큐 활용

```py
def BFS(G, v):# 그래프 G와 탐색 시작점 v
    visited = [0]*(n+1) # n:정점의 개수
    queue = [] # 큐 생성
    queue.append(v) # 시작점 v를 큐에 삽입
    while queue: # 큐가 비어있지 않은 경우
        t = queue.pop(0) # 큐의 첫번째 원소 반환
        if not visited[t]: # 방문되지 않은 곳이라면
            visited[t] = True # 방문한 것으로 표시
            visit(t) # 정점 t에서 할일
            for i in G[t]: # t와 연결된 모든 정점에 대해
                if not visited[i]: # 방문되지 않은 곳이라면
                    queue.append(i) # 큐에 넣기

```
    - BFS는 맞으면 yes, 틀리면 no 알고리즘을 모든 곳에서 똑같이 반복할려고 한다. 그 대상을 어딘가에 저장할려고
    하는데 이걸 스택에 넣을래? 큐에 넣을래? 차이이다. 만약 1번 노드에서 찾아보니 2와 3이 맞다고 할때, 2번과 3
    번 중 어디를 갈지 정해야한다. 스택은 나중에 조사한 3번이 추가되고, 큐는 먼저 조사한 2번이 우선으로 추가
    될 것이다.
    BFS는 내가 갈 수 있는 모든 방향에 대해서 동등한 수준의 탐색 우선순위를 달아준다.
    DFS와 BFS는 상황에 따라, 대상에 따라 서야한다.
    DFS는 다 해봐야지만 알 수 있다.
    BFS는 최단거리에 대해 기록하면서 이동하므로 연산 누적 횟수는 적다
    BFS 어따 씀? -> 길찾기에 사용, 최단경로

# Tree
- 트리
  - 비선형 구조
  - 원소들간의 1:n 관계를 가지는 자료구조
  - 원소들 간의 계층관계를 가지는 계층형 자료구조
  - 상위 원소에서 하위 원소로 내려가면서 확장되는 트리모양의 구조
  - 한 개 **이상의** 노드로 이루어진 유한집합
    - 노드 중 최상위 노드를 루트라 함,정점(노드,버텍스),단말노드_잎노드_leaf
    - 나머지 노드들은 n개의 분리집합으로 분리가능
    - 이 분리집합들은 하나의 트리(재귀적 정의), 루트의 서브트리라고 함            
    -  노드, 간선_부모노드와 자식노드를 연결, 루트노드
    -  형제노드_같은 부모의 자식노드,조상노드_루트 노드까지 경로에 있는 모든 노드, 서브트리, 자손노드_서브트리에 있는 하위레벨의 노드들
    - 차수: 노드에 연결된 자식 노드의 수
      - 트리의 차수: 트리에 있는 노드의 차수 중에서 가장 큰 값.
      - 단말 노드: 차수가 0인 노드, 자식노드가 없는 노드
    - 노드의 높이: 루트에서 노드에 이르는 간선의 수. 노드의 레벨. 초기값 설정은 0이나 1 
    - 트리의 높이: 트리에 있는 노드의 높이 중에서 가장 큰 값

# 이진 트리
    - 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
    - 각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리_왼,오 자식노드. 나머지는 정의하기 나름
    - 레벨 i에서의 노드의 최대 개수는 2**i
      - 높이가 h인 이진트리가 가질 수 있는 노드의 최소 개수는 h+1개가 되며 최대 개수는 2**(h+1)-1개가 된다.

    - 포화 이진 트리
      - 모든 레벨에 노드가 포화상태로 차 있는 이진트리
      - 높이가 h일 때 최대의 노드 개수인 (2**(h+1)-1)의 노드를 가진 이진트리
      - 루트를 1번으로 하여 2**(h+1)-1 까지 정해진 위치에 대한 노드번호를 가짐. 다른 이진트리의 경우 노드번호가 순서대로 안나올 수 있음

    - 완전 이진 트리
      - 높이가 h이고 노드 수가 n개일 때 (2**h <= n <= 2**(h+1)-1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진트리

    - 편향 이진 트리
      - 비효율적인 구조
      - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식노드만을 가진 이진트리_왼쪽편향, 오른쪽 편향 이진트리

    - 순회
      - 트리의 각 노드를 중복되지않게 전부 방문하는 것. 비선형 구조이기 때문에 선후 연결관계를 알 수 없음
      - 전위 순회
        - 부모노드 방문(처리 ) 후 자식노드를 좌우 순서로 방문
          - 현재 노드 n을 방문하여 처리 (V)
          - 현재 노드 n의 왼쪽 서브트리로 이동(L)
          - 현재 노드의 n의 오른쪽 서브트리로 이동(R)
      - 중위 순회
        - 왼쪽 자식 노드, 부모노드, 오른쪽 자식 노드순으로 방문
          - 현재 노드 n의 왼쪽 서브트리로 이동:L
          - 현재 노드 n을 방문하여 처리:V
          - 현재 노드 n의 오른쪽 서브트리로 이동:R
      - 후위 순회
        - 자식노드를 좌우 순서로 방문한 후, 부모노드로 방문
            - 현재 노드 n의 왼쪽 서브트리로 이동한다:L
            - 현재 노드 n의 오른쪽 서브트리로 이동한다:R
            - 현재 노드 n 방문 처리
        - 루트가 마지막으로 처리
  - 배열을 이용한 이진 트리의 표현
    - 이진 트리에 각 노드 번호를 다음과 같이 부여
    - 루트의 번호를 1로함
    - 레벨 n에 있는 노드에 대하여 왼쪽부터 오른쪽으로 2**n - 2**(n+1)-1까지 번호를 차례로 부여

    - 노드 번호의 성질
      - 노드 번호가 i인 노드의 부모노드 번호 i/2
      - 노드 번호가 i인 노드의 왼쪽 자식 노드번호 2*i
      - 노드 번호가 i인 노드의 오른쪽 자식 노드번호 2*i+1
      - 레벨 n의 노드번호 시작번호 2*n
    - 인덱스를 부모번호로 해서 자식번호를 저장.
    - 자식번호를 인덱스로 부모번호를 저장.
    - 부모가 없으면 루트. 루트번호는 무조건 1이 아님. 다를 수 있음.
    - 루트찾기
      - 부모가 없을 때까지 조상 탐색
  - 연결리스트
    - left,right에 왼쪽 자식노드, 오른쪽 자식노드 저장

간선의 개수 = 총 정점의 개수 -1
```py
def pre_order(T):
    if T:
        print(T,end = ' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input())
E = N-1
arr = list(map(int,input().split()))
left = [0]*(N+1)# 부모를 인덱스로 왼쪽 자식번호 저장
right = [0]*(N+1)
par = [0]*(N+1) #자식을 인덱스로 부모 저장

for i in range(E):
    p,c = arr[i*2],arr[i*2+1]
    if left[p]==0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c] != 0:
    c = par[c] # 부모를 새로운 자식으로 두고
root = c  #더이상 부모가 없으면  root
print(root)
pre_order(root)
```

```py
V = int(input())
edge = list(map(int,input().split()))
E = len(edge)
adj = [[] for _ in range(V+1)]
tree = [[0,0] for _ in range(V+1)]

for idx in range(E//2)
    adj[edge[idx*2].append(edge[idx*2+1])]
print(idj)
``` 
자식의 번호를 받을 때 특정 값을 받을 경우 패스
```py
V = int(input())
edge = list(map(int,input().split()))
E = len(edge)
adj = [[] for _ in range(V+1)]
tree = [[0,0] for _ in range(V+1)]

for idx in range(E//2)
    if tree[edge[idx*2]][0] == 0:
        tree[edge[idx*2]][0] = edge[idx*2+1]
    else:
        tree[edge[idx*2]][1] = edge[idx*2+1]
    
print(idj)

def solution(k):
    print(k, end = ' ')

def preorder(now):
    if now != 0:
        solution(now)
        preorder(tree[now][0])
        preorder(tree[now][1])

def inorder(now):
    if now != 0:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])

def postorder(now):
    if now != 0:
        
``` 

탐색 = 연결돼있으면 남김없이 다 돌기
순회 = 그 정점을 루트로 하는 서브트리 내에서만



## 수식 트리
    - 수식을 표현하는 이진 트리
    - 연산자는 루트노드이거나 가지노드
    - 피연산자는 모두 리프노드

## 이잔 탐색 트리
    - 모든 원소는 서로 다른 유일한 키를 갖는다
    - key(왼쪽 서브트리)<key(루트노드)<(오른쪽 서브트리)
    - 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색트리
    - 중위 순회하면 오름차순으로 정렬된 값을 얻을 수있음
  - 탐색 연산
    - 루트에서 시작
    - 탐색할 키 값 x를 루트노드의 키 값과 비교
      - 키 값 x = 루트노드의 키 값인 경우: 원하는 원소를 찾았으므로 탐색연산 성공
      - 키 값 x < 루트노드의 키 값인 경우: 루트노드의 왼쪽 서브트리에 대해서 수행
      - 아님 오른쪽
  - 삽입 연산
    - 먼저 탐색연산을 수행
      - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로 같은 원소가 트리에 있는 지 탐색하여 확인한다
      - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 된다
    - 탐색 실패한 위치에 원소를 삽입
  - 삭제 연산
    - 자식이 없거나 하나만 있으면 삭제하고 연결.
    - 루트 삭제 시 왼쪽 서브트리의 제일 큰 값이나 오른쪽 서브트리의 가장 작은값을 루트에 가져옴
  - 성능
    - 탐색,삽입,삭제 시간은 트리의 높이만큼 시간이 걸린다
      - O(h),h: BST의 깊이(height)
    - 평균의 경우
      - 이진트리가 균형적으로 생성되어있는 경우
      - O(log n)
    - 최악의 경우
      - 한쪽으로 치우친 경사 이진트리의 경우
      - O(n)
      - 순차탐색과 시간복잡도가 같다

    - 배열에서의 순차 탐색:O(N)
    - 정렬된 배열에서의 순차 검색:O(N)
    - 정렬된 배열에서의 이진 탐색:O(log N)
      - 고정 배열 크기와 삽입, 삭제 시 추가 연산 필요
    - 이진트리는 위에 성능
    - 해쉬검색: O(1)
      - 추가 저장공간이 필요
## 힙
    - 완전 이진 트리에 있는 노드 중에서 키값이 가장 큰 노드나 키값이 가장 작은 노드를 찾기 위해서 만든 자료구조
    - 형제노드끼리는 상관 없음

    - 최대 힙
      - 키값이 가장 큰 노드를 찾기 위한 완전 이진 트리
      - 부모노드의 키값 > 자식노드의 키 값
      - 루트노드: 키 값이 가장 큰 노드
    - 최소 힙
      - 키 값이 가장 작은 노드를 찾기 위한 완전 이진트리
      - 부모노드의 키값< 자식노드의 키값
      - 루트노드: 키값이 가장 작은 노드
    - 삽입연산
      - 자리바꾸기
    - 삭제연산
      - 힙에서는 루트노드의 원소만을 삭제할 수 있다
      - 루트노드의 원소를 삭제하여 반환
      - 힙의 종류에 따라 최대값 또는 최소값을 구할 수 있다
```py
def enq(n):
    global last
    last += 1 # 마지막 노드 추가(완전 이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last #부모 > 자식 비교를 위해
    p = c//2 # 부모 번호 계산
    while p >=1 and h[p] <h[c]:
        h[p],h[c] = h[c],h[p]
        c = p
        p = c//2

def deq():
    glpbal last
    tmp = h[last] # 루트의 키값 보관
    h[1] = h[last]
    last -= 1
    p = 1   #새로 옮긴 루트
    c = p*2
    while c <= last:
        if c + 1 <= last and h[c] < h[c+1]: #오른쪽 자식이 있고 더 크면
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c],h[p]
            p = c
            c = p*2
        else:
            break
    return temp

N = 10
h = [0]*(N+1)
last = 0
enq(2)
enq(5)
enq(3)
enq(6)
enq(4)
while last>0:
    print(deq())
```







- 당구, 눈빛, 엄숙, 롤드컵, 