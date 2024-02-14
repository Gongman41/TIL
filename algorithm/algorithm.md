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
def bubble_sort(numbers):
    # n-1 번째 까지 조사를 해나갈 것.
    # range(start, end, step)
    # -> start : 작성된 정수 부터 시작
    # -> end : 작성된 정수 - step 까지
    # -> step : 다음 정수의 값
    for i in range(len(numbers) - 1, 0, -1):#처음이 반대
        # 이번 회차에 조사 해야 할 범위
        for j in range(i):
            # print(numbers[j], numbers[j+1])
            # j가 다음 위치 보다 값이 크면 (오름차순 기준)
            if numbers[j] > numbers[j + 1]:
                # 둘의 값을 바꿔치기 한다.
                # tmp = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = tmp
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                print(numbers, numbers[j], numbers[j + 1])
    return numbers

numbers = [55, 7, 78, 12, 42]

print(bubble_sort(numbers))
```

버블 정렬이나 앞에애들이랑 뒤에 한놈이랑 비교하는 거나 별 차이 없는 거 같은데..?

#카운팅 정렬
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
        counts[data[i]] -= 1#인덱스로 쓸려면 하나씩 마이너스
    temp[counts[data[i]]] =  data[i]
    print(*temp)
    ```
```py
def counting_sort(input_arr, k):
    """
    input_arr : 입력 배열(1 to k)
    counting_arr : 카운트 배열
    k는 데이터의 개수가 아닌 데이터 원소의 범위
    """

    counting_arr = [0] * (k + 1)

    # 1. counting array에 arr내 원소의 빈도수 담기
    for i in range(0, len(input_arr)):
        counting_arr[input_arr[i]] += 1
    # for i in input_arr:
    #     counting_arr[i] += 1

    # 2. 누적(counting_arr 업데이트)
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    # 3. result_arr 생성
    result_arr = [-1] * len(input_arr)

    # 4. result_arr에 정렬하기(counting_arr를 참조)
    for i in range(len(result_arr) - 1, -1, -1):
        counting_arr[input_arr[i]] -= 1
        result_arr[counting_arr[input_arr[i]]] = input_arr[i]
    # for i in input_arr:
    #     counting_arr[i] -= 1
    #     result_arr[counting_arr[i]] = i

    return result_arr


a = [0, 4, 1, 3, 1, 2, 4, 1]

print(counting_sort(a, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]
```
## 완전검색
- 모든 경우의 수를 나열해보고 확인하는 기법
- 경우의 수가 상대적으로 작을 때 유용
- 수행속도 느림, 해답 찾아내지 못할 확률이 낮음

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
    - 지그재그 순허ㅣ
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

```py
'''
10
-7 -5 2 3 8 -2 4 6 9
'''
N = 100
# arr = list(map(int,  '-7 -5 2 3 8 -2 4 6 9 0'.split()))
arr = list(range(1, 101))
# 부분집합의 합이 55 미만인 경우만 모은 리스트
# print(arr)
print(2**N)
# print(1 << N)
# print(bin(1024))
# for i in range(1, 1 << N):
#     lst = []
#     print(i, '번째 경우의 수')
#     for j in range(N-1, -1, -1):
#         if i & (1 << j):
#             lst.append(arr[j])
#             if sum(lst) >= 55:  # 부분집합의 합이 55이상이 되면조사 종료
#                 break
#     if sum(lst) < 55:   # 부분집합의 합이 55 미만인 경우만 출력
#         print(lst)
        # print(1 << j)
        # i번째 경우의 수에, j번째 요소가 포함 되어있는 부분집합인지 확인하는코드
        # i번째가 3번째라면 -> 0b 0011
        # j번쨰 요소 (0번쨰, 1번째, 2번째...) -> 0b 0001, 0010, 0011
        # if i & (1 << j):
        #     lst.append(arr[j])
    # if sum(lst) == 0:
    #     print(lst)
    #     print('있어용')
    #     break
    # print(lst)

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
    배열의 k번째를 반환한다. 셀렉트소트로 앞쪽으로 이동.필요한만큼만 정렬이구나
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

                
    
    
    

            
