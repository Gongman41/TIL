from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
num = 0
q = deque([1])
visited = [0]*(N+1)
visited[1] = 1

while q:
    cur = q.pop()
    for next in lst[cur]:
        if not visited[next]:
            q.append(next)
            visited[next] = 1
            num += 1
    
print(num)
