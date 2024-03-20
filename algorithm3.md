## 알고리즘 설계 기법의 종류
- 완전 탐색
  - 배열: for문, while 문
  - 그래프(관계가 있는 데이터)
    - DFS,BFS
  
완전탐색을 구현하면 시간 or 메모리 초과가 되더라

- 상황마다 좋은 걸 고르자 (그리디)
  - 규칙 + 증명 -> 구현

- 큰 문제를 작은 문제로 나누어 부분적으로 해결하자(다이나믹 프로그래밍)
  - 분할정복과 다르게 작은 문제가 중복
  - 중복된 문제의 해답을 저장해놓고 재활용하자(메모이제이션)

- 큰 문제를 작은 문제로 나누어 부분적으로 해결하자(분할정복)
- 전체중 가능성 없는 것을 빼자(백트래킹)

인천 자취방 가스 끊기

## 분할정복
- 문제를 분할해서 해결
- 분할_나눌수 없을 때까지, 정복, 통합
  - 하나라도 틀리면 전체결과 잘못나옴
  - 비슷한 로직을 반복
  - 보통 재귀로 구현
  
### 병합 정렬
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 자료를 최소 단위의 문제까지 나눈 후에 병합하면서 차례대로 정렬하여 최종 결과를 얻어냄
- O(n log n)
- 이진이랑 비슷하게 가는데 나눠서 그 리스트를 다시 재귀. 다 돌리면 병합
- 병합 시에는 크기 비교
- 멀티코어 CPU 나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기위해 사용

### 퀵 정렬
- 분할할 떄 기준 아이템 중심으로 분할, 병합은 필요 x
- 평균적으로 효율 개좋음
- 호아 파티션 알고리즘
  - 가운데로 위치시킨 p(피봇)값보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치
  - 피봇값은 왼쪽 끝 오른쪽 끝 임의의 세 값중에 중간값
  - i는 가다가 큰값 만나면 정지, j는 반대에서 오다가 작은값 만나면 정지. 교환.
  - 최종 정지한 위치의 값과 피봇값 교환
- 로무토_별로임

- 매우 큰 입력 데이터에 대해서 좋은 성능

- 근데 sort()는 nlog n 이 보장됨. 그냥 sort()써라


### 이진 검색
- 자료는 정렬된 상태여야됨.
```py
arr = [324,32,22114,16,48,93,422,21,316]
arr.sort()
#반복문 버전
def binartSearch(target):
  # 제일 왼쪽, 오른쪽 인덱스 구하기
  low = 0
  high = len(arr) - 1

  # 해당 숫자를 찾으면 종료
  # 더 이상 쪼갤 수 없을 때까지
  while low <= high:
    mid = (low+high)//2

    # 가운데 숫자가 정답이면 종료
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      high = mid - 1
    elif arr[mid] < target:
      low = mid + 1
  return -1 
print(binarySearch(21))

# 재귀함수버전
def bibinarySearch(low,high, target):
  #기저조건(언제까지 재귀가 반복되어야 할까)
  if low > high:
    return -1
  
  #다음 재귀 들어가기 전엔 무엇을 해야할까
  #정답 판별
  mid = (low+high)//2
  if target == arr[mid]:
    return mid
  
  #다음 재귀 함수 호출 (파라미터 생각 잘하기)
  if target < arr[mid]:
    return binartSearch(low, mid -1, target)
  else:
    return binarySearch(mid+1, high, target)
  #재귀 함수에서 돌아왔을 때ㅔ 어떤 작업을 해야할까
  #이진 검색에서는 없다.


```

lower bound, upper bound.

## 백트래킹 응용
- 완전탐색 + 가지치기. 가능성이 없는 경우의 수를 제거
```py
# 재귀함수 팁: 파라미터는 바로 작성하지 않고 구조를 먼저 잡으면 필요한 변수들이 보임
arr = [i for i in range(1,4)]

def dfs(level):
  if level == 3: 
    return path
  #재귀함수 호출
  for i in range(len(arr)):
    if arr[i] in path:
      continue
    path[level] = arr[i]
    dfs(level+1)
    path[level] = 0
    # path[level] = 1
    # dfs(level+1)

    # path[level] = 2
    # dfs(level+2)
    
    # path[level] = 3
    # dfs(level+3)
   
```
- 시간복잡도: 계산하기 힘듦. 최악의 경우 완전탐색

## 트리
- 싸이클이 없는_형제 노드끼리는 연결x_ 무향 연결 그래프
- 그래프도 트리로 표현 가능
- 차수_후보군의 수, 높이_시간복잡도

## 이진트리
- 최대 2개의 서브트리
- 노드의 개수가 N개일 때 이진트리의 높이
  - 최악 N, 최선 log N
- 포화 이진트리: 모든 노드가 자식 꽉 참
- 완전 이진트리: 왼쪽부터 잘참

```py
nodes = [[] for _ in range(14)]
for i in range(0,len(arr),2):
  parent_node = arr[i]
  child_node = arr[i+1]
  nodes[parent_node].append(child_node)
for li in nodes:
  for _ in range(len(li),2)
    li.append(None)

def inorder(nodeNum):
  if nodeNum == None:
    return
  inorder(nodes[nodeNum][0])
  print(nodeNum, end=' ')
  inorder(nodes[nodeNum][1])

```

## 이진탐색트리(BST)
- 탐색용 트리
- 탐색연산의 횟수 = 트리의 높이
- 삽입연산: 탐색실패 위치
- 삭제연산
  - 차수가 0인 경우: 없애기
  - 차수가 1인 경우: 없애고 연결
  - 차수가 2인 경우: 작은 것 중에서 제일 큰거

## 힙트리
- 키 값이 가장 큰 노드나 키 값이 가장 작은 노드를 찾기 위해 만든 자료구조
- 최대 힙: 부모노드의 키 값 > 자식노드의 키 값
- 최소 힙: 반대
- 삽입: 일단 마지막에 넣기 -> 부모 비교. 최악의 경우 O(h)
- 삭제: 루트노드만 삭제 가능
  - 마지막 노드 넣고 자리바꾸기
  - heapq

## 그래프
- 노드 + 간선으로 이루어진 자료구조_데이터 간 관계를 표시하기위해
- N:N 관계를 가지는 원소들을 표현하기에 용이하다
- 그래프 유형
  - 무향 그래프_양방향
  - 유향 그래프
  - 가중치 그래프_가중치 혹은 비용. 다익스트라,최소비용 문제에 사용
  - 사이클이 없는 방향 그래프
  - 생긴 유형
    - 완전 그래프: 정점들에 대해 가능한 모든 간선들을 가진 그래프
    - 부분 그래프: 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프
  - 인접: 두 개의 정점에 간선이 존재하면 인접_그래프
  - 경로: 간선들을 순서대로 나열
    - 한번만 지나면 단순경로
    - 다시 돌아올 수 있다면 싸이클
```py
# 인접 행렬
# 장점:행렬곱을 이용해서 탐색 쉽게 가능, 노드간의 연결 정보를 한 방에 확인 가능, 간선이 많을수록 유리
# 단점: 노드 수가 커지면 메모리가 낭비_연결이 안된것도 저장하기 때문에
# -> 노드 수, 메모리 제한 확인
# 양방향 그래프는 우하단 대각선 기준으로 대칭됨
graph = [
  [0,1,0,1,0],
  # 0은 1과 3으로 갈 수 있다
  [1,0,1,0,1],
  [0,1,0,0,0],
  [1,0,0,0,1],
  [0,1,0,1,0],
]

# 인접리스트
# V개의 노드가 갈 수 있는 정보만 저장
# 장점: 메모리 사용량이 적다, 탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율
# 단점: 특정 노드 간 연결여부를 확인하는 데 시간이 걸린다.
graph = [
  [1,3],
  [0,2,4],
  [1],
  [0,4],
  [1,3],
]

```
- 인접 행렬 DFS: 재귀
```py
graph = [
  [0,1,0,1,0],
  [1,0,1,0,1],
  [0,1,0,0,0],
  [1,0,0,0,1],
  [0,1,0,1,0],
]

visited = [0]*5
path = []
def dfs(now):
  # 기저 조건
  # 지금 문제에선 없다

  # 다음 재귀 호출 전, 재귀 호출 후
  # visited[now] = 1
  # path/append(now)
  print(now, end=' ')

  # 다음 재귀 호출. 가기전에 작업
  # dfs: 현재 노드에서 다른 노드들을 확인
  # 다른 노드들 == 반복문
  for to in range(5):
    # 갈 수 없다면 pass
    if graph[now][to] == 0:
      continue
    # 이미 방문했다면
    if visited[to]:
      continue
    
    visited[to] = 1
    path.append(to)
    dfs(to)
    # visited[to] = 0 백트래킹

  # 돌아왔을 때 작업
  # 출발점에 대한 visited
visited[0] = 1
path.append(0)

dfs(0) 
```

- 인접 리스트
```py
graph = [
  [1,3],
  [0,2,4],
  [1],
  [0,4],
  [1,3],
]

visited = [0]*5
path = []
def dfs(now):
  # 기저 조건
  # 지금 문제에선 없다

  # 다음 재귀 호출 전, 재귀 호출 후
  # visited[now] = 1
  # path/append(now)
  print(now, end=' ')

  # 다음 재귀 호출. 가기전에 작업
  # 인접리시트
  # 차이점 1. 갈수 없는 곳 조건 필요없음
  # 차이점 2. for문 작성 수정
  for to in graph[now]:
    # 이미 방문했다면
    if visited[to]:
      continue
    
    visited[to] = 1
    path.append(to)
    dfs(to)
    # visited[to] = 0 백트래킹

  # 돌아왔을 때 작업
  # 출발점에 대한 visited
visited[0] = 1
path.append(0)

dfs(0) 
```

- 인접 행렬 BFS
  
```py
graph = [
  [0,1,0,1,0],
  [1,0,1,0,1],
  [0,1,0,0,0],
  [1,0,0,0,1],
  [0,1,0,1,0],
]

def bfs(start):
  visited = [0] * 5
  
  queue = [start]
  visited[start] = 1
  
  while queue:
    now = queue.pop(0)
    print(now, end=' ')

    # 갈 수 있는 곳을 체크
    for to in range(5):
      if graph[now][to] == 0:
        continue
      if visited[to]:
        continue
      visited[to] = 1
      queue.append(to) 
      # 
```

- 인접리스트 BFS_ 이게 더 편하다. 딕셔너리 활용해볼 것. 쓰는 이유도
```py
graph = [
  [1,3],
  [0,2,4],
  [1],
  [0,4],
  [1,3],
]

def bfs(start):
  visited = [0] * 5
  
  queue = [start]
  visited[start] = 1
  
  while queue:
    now = queue.pop(0)
    print(now, end=' ')

    # 갈 수 있는 곳을 체크
    for to in graph[now]:
      
      if visited[to]:
        continue
      visited[to] = 1
      queue.append(to) 
      # 
```

## union-find(disjoint set)
- 서로소 집합: 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들, 즉 교집합이 없다_니네편인지 우리편인지. 관계존재
- 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분. 이를 대표자라 함
- 표현 방법
  - 연결리스트
  - 트리
- 상호배타 집합 연산
  - Make-Set(x): 집합 만들기. 처음엔 자기자신이 대표
  - Find-Set(x): 너네 대표 누구야
  - Union(x,y): 같은 집합으로 묶자. 한쪽의 대표자가 다른 집합에 속한걸로
- 트리
  - 루트가 집합의 대표자
  
```py
def make_set(x):
  parent = [i for i in range(n)]
  rank = [0]*x
  return parent, rank
  # 자기자신이 대표인 데이터 6개가 리스트로 생성. 숫자는 대표자 인덱스를 의미.
parent, rank = make_set(7)
def find_set(x):
  # 부모노드도 연결이 되어있다면 다시 반복. 자기자신이 대표인 데이터를 찾을 때까지.
  if parent[x] == x:
    return x
  # 위의 조건이 걸리지 않았다 == 대표자가 따로 있다
  return find_set(parent[x])

def union(x,y):
  root_x = find_set(x)
  root_y = find_set(y)
  # 이미 같은 집합에 속해있다면 continue
  if root_x == root_y:
     
  # 다른 집합이면 합침
  # ex) 더 작은 루트노드에 합쳐라
    if root_x < root_y:
      if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    
    elif root_y < root_x:
      
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
```
- 문제점
- 해결
- 경로압축,랭크