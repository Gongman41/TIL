import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
# 사다리를 최대한 타면서 뱀을 피하기
# 사다리중에 제일 잘나가는 놈
n_lst = list(range(101))

for _ in range(N):
    s,e = map(int,input().split())
    n_lst[s] = e
    
for _ in range(M):
    s,e = map(int,input().split())
    n_lst[s] = e

q = deque([[1,0]])
visited = [False]*101
visited[1] = True
min_cnt = float('inf')
while q:
    cur,cnt = q.popleft()
    if cnt >= min_cnt:
        continue
    if cur == 100:
        min_cnt = min(cnt,min_cnt)
    
    for i in range(1,7):
        next = cur + i
        if next <= 100 and visited[next] == False:
            q.append([n_lst[next],cnt+1])
            visited[next] = True
print(min_cnt)
        