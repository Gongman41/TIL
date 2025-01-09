import sys
from collections import defaultdict,deque

input = sys.stdin.readline
N,M = map(int,input().split())
# graph = [[0]*(N+1) for _ in range(N+1)]
min_n = [0, float('inf')]
# 딕셔너리로 해야될 거 같은데 기억이 안남. 일단 인덱스로
# for _ in range(M):
#     a,b = map(int,input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# 인접 리스트 생성
graph = defaultdict(list)
# 원래는 graph = {} 이렇게 하고 setdefault로 했었음
# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, N + 1):
    sum_cur = 0
    q = deque([i])
    visited = [False] * (N + 1)
    distance = [0] * (N + 1)
    visited[i] = True

    # while q:
    #     cur = q.popleft()
    #     for k in range(1, N + 1):
    #         if graph[cur][k] == 1 and not visited[k]:
    #             visited[k] = True
    #             q.append(k)
    #             distance[k] = distance[cur] + 1

    while q:
        cur = q.popleft()
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                distance[neighbor] = distance[cur] + 1
    
    sum_cur = sum(distance)
    if sum_cur < min_n[1]:
        min_n = [i, sum_cur]

print(min_n[0])