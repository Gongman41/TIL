import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10**10  # 무한대 값

V, E = map(int, input().split())
K = int(input())

# 인접 리스트 생성
lines = [[] for _ in range(V+1)]
visited = [INF] * (V+1)

# 그래프 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    lines[u].append((v, w))

# 다익스트라 알고리즘 (우선순위 큐 활용)
q = []
heappush(q, (0, K))  # (거리, 노드) 순서로 저장
visited[K] = 0

while q:
    sum_long, cur = heappop(q)

    # 이미 처리된 노드면 무시 (더 긴 경로는 필요 없음)
    if sum_long > visited[cur]:
        continue

    for next, plus_long in lines[cur]:
        new_dist = sum_long + plus_long
        if new_dist < visited[next]:  # 최단 거리 갱신
            visited[next] = new_dist
            heappush(q, (new_dist, next))

# 결과 출력
for i in range(1, V+1):
    print("INF" if visited[i] == INF else visited[i])
