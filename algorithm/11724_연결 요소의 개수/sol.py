import sys
from collections import deque
input = sys.stdin.readline

N , M = map(int,input().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    lst[u].append(v)
    lst[v].append(u)

visited = [False]*(N+1)
cnt = 0
q = deque([])
for i in range(1,N+1):
    if not visited[i]:
        cnt += 1
        visited[i] = True
        q.append(i)
        while q:
            cur = q.popleft()
            for next in lst[cur]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)

print(cnt)
