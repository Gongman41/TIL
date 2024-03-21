# import sys
from heapq import heappush,heappop
# sys.stdin = open('input.txt')
def prim(start):
  pq = []
  MST = [0] * (V+1)
  # 최소 비용
  sum_weight = 0

  heappush(pq,(0,start))
  # 가중치,현재위치 푸시
  while pq:
    weight, now = heappop(pq)
    # 방문했다면
    # 우선순위 큐 특성상(가중치 오름차순) 더 먼거리로 가는 방법이 큐에 저장이 되어 있기때문에 기존에 더 짧은 거리로 방문했다면 CONTINUE
    if MST[now]:continue
    MST[now] = 1
    sum_weight += weight
    # 갈 수 있는 노드들을 보면서
    for to in range(V+1):
      # 갈 수 없거나 이미 반복했다면
      if graph[now][to] == 0 or MST[to]:
        continue
      heappush(pq,(graph[now][to],to))
  print(f'#{tc} {sum_weight}')


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    # 노드간 연결 관계
    for _ in range(E):
        s,e,w = map(int,input().split())
        # 시작노드, 다음노드, 가중치
        graph[s][e] = w
        graph[e][s] = w
    #     양방향
    prim(0)
