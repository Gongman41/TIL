import sys
from collections import deque
input = sys.stdin.readline
V,E = map(int,input().split())
K = int(input())
lines = [[] for _ in range(V+1)]
visited = [10e10]*(V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    lines[u].append((v,w))
visited[K] = 0
q = deque([(K,0)])
while q:
    cur, sum_long = q.popleft()
    for next, plus_long in lines[cur]:
        if visited[next] > sum_long + plus_long:
            visited[next] = sum_long + plus_long
            q.append((next, sum_long + plus_long))

for i in range(1,V+1):
    if visited[i] == 10e10:
        print('INF')
        continue
    print(visited[i])