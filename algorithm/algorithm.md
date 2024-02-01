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
        counts[data[i]] -= 1
    temp[counts[data[i]]] =  data[i]
    print(*temp)
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
 
    
    
    
    
    
            
